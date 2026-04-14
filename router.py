from llm import ask_llm

VALID = ["coding", "automation", "tamil", "study"]

def route_task(user_input):
    text = user_input.lower()

    # ✅ RULE-BASED (HIGH PRIORITY)

    if any(x in text for x in ["what is", "explain", "define"]):
        return "study"

    if any(x in text for x in ["create", "delete", "list", "folder", "file"]):
        return "automation"

    if any(x in text for x in ["run", "execute", "script"]):
        return "automation"

    if "tamil" in text:
        return "tamil"

    if any(x in text for x in ["code", "program", "python", "java"]):
        return "coding"

    # ✅ FALLBACK → LLM
    prompt = f"""
Classify this into ONLY one word:
coding, automation, tamil, study

User: {user_input}

Answer ONLY one word.
"""

    res = ask_llm(prompt).strip().lower()

    for v in VALID:
        if v in res:
            return v

    return "study"