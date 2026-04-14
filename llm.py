import subprocess
from config import MODEL

def ask_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",   # ✅ FIX
            errors="ignore"     # ✅ PREVENT CRASH
        )
        return result.stdout.strip()
    except Exception as e:
        return f"LLM Error: {e}"