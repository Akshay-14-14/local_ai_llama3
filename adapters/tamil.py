from llm import ask_llm

def run(user_input):
    prompt = f"Translate or answer in Tamil: {user_input}"
    return ask_llm(prompt)