# Simple AI Agent (Ollama + Tool Calling)

## Overview

This project is a **minimal AI agent built from scratch** using a local LLM via Ollama.
It demonstrates how an agent can:

* Decide when to use tools
* Execute those tools
* Return reliable, grounded results

The focus is on understanding **core agent architecture**, not using frameworks.

---

## Features

* Local LLM integration (via Ollama)
* Tool calling (calculator, date)
* JSON-based action system
* Custom parser for structured outputs
* Hallucination control using tool grounding
* Debug logging for step-by-step tracing

---

## Project Structure

```
simple-ai-agent/
│
├── agent.py        # Agent loop (decision + execution)
├── parser.py       # Extracts structured JSON from LLM output
├── tools.py        # Available tools (calculator, date)
├── llm.py          # Handles calls to Ollama
├── prompt.py       # System prompt (agent behavior rules)
├── main.py         # CLI interface
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. User Input

User provides a query via CLI.

### 2. LLM Decision

The model returns a JSON action:

```json
{"action": "calculator", "input": "2+2"}
```

### 3. Tool Execution

The agent executes the tool:

```
Result: 4
```

### 4. Final Output

The agent returns the **tool result (trusted)** instead of relying on the LLM.

---

## Why This Matters

LLMs can hallucinate.

This system ensures:

* Tools = **source of truth**
* LLM = **decision maker only**

---

## Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Install and run Ollama

Make sure Ollama is running locally:

```
ollama run phi3
```

### 3. Run the agent

```
python main.py
```

---

## Example

**Input:**

```
What is 2+2?
```

**Output:**

```
4
```

---

## Key Learnings

* Agent loop design (observe → decide → act)
* Tool integration
* Output parsing
* Handling unreliable LLM outputs
* Building without frameworks

---

## Future Improvements

* Add memory (multi-turn conversations)
* Add more tools (web search, file reader)
* Improve prompt robustness
* Introduce multi-step reasoning
* Add retry/fallback mechanisms

---

## Disclaimer

This project uses small local models (e.g., phi3), which may:

* Produce inconsistent outputs
* Ignore instructions occasionally

The system is designed to **handle these limitations gracefully**.

---

## Author

Built as part of learning AI agent systems from scratch.
