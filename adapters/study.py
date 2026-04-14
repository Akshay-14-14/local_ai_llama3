from llm import ask_llm

def run(user_input, context):
    prompt = f"""
You are a teacher.

Context:
{context}

Explain clearly:
{user_input}
"""
    return ask_llm(prompt)