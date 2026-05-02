# Learning Report — Building a Simple AI Agent from Scratch

## Objective

The goal of this project was to **understand how AI agents actually work internally**, rather than relying on frameworks.
This included building:

* an agent loop
* tool execution system
* output parser
* local LLM integration using Ollama

---

## 1. Understanding the Agent Architecture

This project made one thing clear:

> An AI agent is not just an LLM — it is a **system around the LLM**

Core components built:

* **LLM (llm.py)** → generates structured decisions
* **Parser (parser.py)** → extracts usable JSON from messy outputs
* **Tools (tools.py)** → execute real-world actions
* **Agent Loop (agent.py)** → controls flow and enforces correctness

### Key Insight

The LLM is **not the source of truth**.
It is only responsible for deciding *what to do*, not *what is correct*.

---

## 2. Working with Ollama (Local LLMs)

### What was used

* `phi3` (primary model)
* `gemma:1b` (secondary testing)

---

### Pros of Using Ollama

* Runs **locally** (no API cost)
* Easy setup (`ollama run`, `ollama pull`)
* Good for learning agent behavior
* Fast iteration without external dependencies

---

### Cons / Limitations

* Small models → **weak instruction following**
* High hallucination rate
* Poor formatting consistency (especially JSON)
* Tendency to:

  * generate extra text
  * ignore constraints
  * drift into unrelated instructions

---

### Key Learning

> Local small models require **strong system design**, not just good prompts.

---

## 3. Prompt Engineering (Trial & Error)

Initial assumption:

> “If the prompt is strict enough, the model will behave correctly”

This turned out to be false.

---

### Observed Issues

* Model returned:

  * multiple JSON objects
  * extra explanations
  * completely unrelated instructions
* Ignored rules like:

  * “only output JSON”
  * “do not generate multiple responses”

---

### Iterations Made

* Simplified instructions
* Added strict formatting rules
* Added tool usage constraints
* Reduced prompt size to avoid confusion

---

### Key Learning

> Prompting alone is **not sufficient** to control LLM behavior.

You must:

* constrain inputs
* control outputs
* validate responses

---

## 4. Parser Design (Critical Component)

The parser became one of the most important parts of the system.

---

### Initial Problem

Model outputs looked like:

```json
{"action": "date"}
{"action": "final", "output": "wrong date"}
```

A naive parser would:

* pick the first JSON
* or pick the final answer blindly

Both approaches caused failures.

---

### Solution

* Extract **all JSON blocks**
* Apply **priority logic**:

  1. Tool actions
  2. Final answer

---

### Key Learning

> You must assume LLM output is **noisy and unreliable**

The parser acts as a **control layer**, not just a utility.

---

## 5. Agent Loop Design

Initial design used a full loop:

```text
LLM → Tool → LLM → Final
```

---

### Problems Faced

* Infinite loops
* Repeated tool calls
* Failure to stop
* Ignoring tool results

---

### Final Design Decision

Simplified to:

```text
LLM → Tool → Return result
```

---

### Why This Works Better

* Removes unnecessary dependency on LLM
* Eliminates hallucinated final answers
* Ensures deterministic output

---

### Key Learning

> Simpler control flow = more reliable system (especially with small models)

---

## 6. Tool Grounding (Most Important Concept)

A major breakthrough in this project:

> Tools must override the LLM

---

### Example

LLM output:

```json
{"action": "date"}
{"action": "final", "output": "2023-04-15"}
```

Tool output:

```
2026-05-02
```

---

### Correct behavior:

Return:

```
2026-05-02
```

---

### Key Learning

> LLM answers are suggestions.
> Tool outputs are **facts**.

---

## 7. Debugging & Observability

Adding debug logs was essential:

* Prompt visibility
* Raw LLM output
* Parsed result
* Tool execution

---

### Key Learning

> Without logs, debugging agents is guesswork.

---

## 8. Model Limitations (Reality Check)

Even after all fixes:

* Models still:

  * hallucinate
  * break formatting
  * inject unrelated instructions

---

### Important Realization

> You don’t fix models — you design systems that handle their weaknesses.

---

## 9. System Design Lessons

This project reinforced several core engineering principles:

---

### 1. Separation of Concerns

| Component | Responsibility    |
| --------- | ----------------- |
| LLM       | decision making   |
| Parser    | structure control |
| Tools     | execution         |
| Agent     | orchestration     |

---

### 2. Never Trust Raw LLM Output

Always:

* parse
* validate
* control

---

### 3. Determinism > Intelligence

A simpler, predictable system is better than:

* a “smart” but unreliable one

---

### 4. Reduce Complexity Early

Start simple:

* single-step agent
* minimal tools

Then scale.

---

## 10. What Could Be Improved

* Add memory (conversation history)
* Add more tools (search, APIs)
* Introduce retry mechanisms
* Improve parsing robustness
* Move toward multi-step reasoning safely

---

## Final Takeaway

This project shifted the understanding of AI agents from:

> “Using an LLM to get answers”

to:

> “Building a system that controls an LLM to produce reliable outcomes”

---

## Summary

Key concepts learned:

* Agent loop design
* Tool-based reasoning
* Prompt limitations
* Parsing strategies
* System reliability over model capability
* Working with local LLMs (Ollama)

---

## Closing Thought

The most important insight from this project:

> **Good AI systems are not built by trusting the model —
> they are built by controlling it.**
