from llm import call_llm
from prompt import SYSTEM_PROMPT
from parser import parse_llm_output
from tools import TOOLS


def run_agent(user_input: str, model="phi3", max_steps=5, debug=False):
    history = ""

    for step in range(max_steps):
        if debug:
            print(f"\n--- STEP {step+1} ---")

        # Build prompt
        if not history:
            prompt = SYSTEM_PROMPT + user_input + "\nAssistant:"
        else:
            prompt = SYSTEM_PROMPT + history

        if debug:
            print("\n[Prompt]")
            print(prompt[-500:])

        # Call LLM
        llm_output = call_llm(prompt, model=model)

        if debug:
            print("\n[LLM Output]")
            print(llm_output)

        # Parse response
        parsed = parse_llm_output(llm_output)

        if debug:
            print("\n[Parsed Output]")
            print(parsed)

        action = parsed.get("action")

        # ✅ CASE 1: Tool call → ALWAYS execute
        if action in TOOLS:
            tool_input = parsed.get("input", "")
            tool_function = TOOLS[action]

            if debug:
                print(f"\n[Tool Call] {action}({tool_input})")

            tool_result = tool_function(tool_input)

            if debug:
                print(f"[Tool Result] {tool_result}")

            # 🔥 RETURN IMMEDIATELY (skip LLM final completely)
            return str(tool_result)

        # ✅ CASE 2: Final answer (only if NO tool used)
        elif action == "final":
            if debug:
                print("\n[FINAL ANSWER]")
            return parsed.get("output")

        else:
            return "Error: Unknown action from LLM"

    return "Error: Max steps reached"