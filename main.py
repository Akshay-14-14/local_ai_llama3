import os
from router import route_task
from adapters import coding, automation, tamil, study
from rag import retrieve
from memory import save
from config import BASE_DIR


def main():
    # ✅ Ensure correct working directory
    os.chdir(BASE_DIR)

    print("🧠 Local AI (Offline + Sandbox + Multi Adapter)")

    while True:
        try:
            user = input("\nYou: ").strip()

            # ✅ Exit condition
            if user.lower() in ["exit", "quit"]:
                print("👋 Exiting AI...")
                break

            if not user:
                continue  # skip empty input

            # ✅ Route task
            task = route_task(user)
            print(f"🧭 Task detected: {task}")  # Debug

            # ✅ Retrieve RAG context safely
            context = retrieve(user)
            if not context:
                context = ["No relevant context found"]

            # ✅ Execute based on adapter
            if task == "coding":
                res = coding.run(user, context)

            elif task == "automation":
                res = automation.run(user)

            elif task == "tamil":
                res = tamil.run(user)

            elif task == "study":
                res = study.run(user, context)

            else:
                res = "⚠️ Unknown task type"

        except Exception as e:
            res = f"❌ Error: {str(e)}"

        # ✅ Output result
        print("\n🤖:", res)

        # ✅ Save memory safely
        try:
            save(user, res)
        except Exception as e:
            print("⚠️ Memory save failed:", e)


if __name__ == "__main__":
    main()