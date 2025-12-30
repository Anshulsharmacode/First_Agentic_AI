# AgenticAI

This is my **first Agentic AI project**.

Small demo agent that uses LangChain + Google Generative AI (Gemini) to run tools.  
Primary purpose: demo registering a simple tool (open_webpage) and invoking an LLM-backed agent.

---

## Files

- `main.py` — Agent setup and example run. Registers an `open_webpage(url: str)` tool and initializes a ChatGoogleGenerativeAI LLM.

---

## Prerequisites

- Linux / macOS / Windows (commands below assume Linux)
- Python 3.10+
- A Google Generative AI API key (set in `GOOGLE_API_KEY` environment variable)
- Display/X server if you want `webbrowser.open()` to actually open a GUI browser (or use a headful container/desktop).

---

## Quick setup (recommended)

```bash
# create + activate venv (Linux/macOS)
python -m venv .venv
source .venv/bin/activate


pip install -r requirement.txt

-------------OR------------------

pip install langchain langchain-google-genai
```
