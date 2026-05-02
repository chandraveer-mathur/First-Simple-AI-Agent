import json
import re


def extract_all_json(text: str):
    """
    Extract all JSON objects from text.
    """
    matches = re.findall(r"\{.*?\}", text, re.DOTALL)
    results = []

    for m in matches:
        try:
            results.append(json.loads(m))
        except:
            continue

    return results


def parse_llm_output(output: str):
    """
    Parse LLM output intelligently.

    PRIORITY:
    1. Tool actions
    2. Final answer
    """

    json_blocks = extract_all_json(output)

    if not json_blocks:
        return {
            "action": "final",
            "output": "Error: could not parse response"
        }

    # ✅ PRIORITY 1: TOOL CALL
    for block in json_blocks:
        action = block.get("action")
        if action in ["calculator", "date"]:
            return {
                "action": action,
                "input": block.get("input", "")
            }

    # ✅ PRIORITY 2: FINAL ANSWER
    for block in json_blocks:
        if block.get("action") == "final":
            return {
                "action": "final",
                "output": block.get("output", "")
            }

    # fallback
    return {
        "action": "final",
        "output": "Error: invalid response format"
    }