from llm import ask_llm

def run(user_input, context):
    prompt = f"""
You are a smart coding assistant.

Context:
{context}

User request:
{user_input}

Instructions:
- If the user asks for explanation → explain clearly (no code)
- If the user asks for code → provide clean code
- If both → explain first, then give code
- Do NOT generate code unnecessarily

Answer:
"""
    return ask_llm(prompt)