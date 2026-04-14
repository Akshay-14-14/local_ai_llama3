from sandbox import *
import re

def extract_name(text):
    words = text.split()
    if len(words) > 2:
        return words[-1]
    return None


def run(user_input):
    text = user_input.lower()

    # ✅ CREATE FOLDER
    if "create" in text and "folder" in text:
        name = extract_name(user_input) or input("Folder name: ")
        return create_folder(name)

    # ✅ DELETE FOLDER
    if "delete" in text and "folder" in text:
        name = extract_name(user_input) or input("Folder name: ")
        return delete_folder(name)

    # ✅ CREATE FILE
    if "create" in text and "file" in text:
        name = extract_name(user_input) or input("File name: ")
        return create_file(name)

    # ✅ DELETE FILE
    if "delete" in text and "file" in text:
        name = extract_name(user_input) or input("File name: ")
        return delete_file(name)

    # ✅ LIST
    if "list" in text:
        return list_files()

    # ✅ RUN SCRIPT
    if "run" in text:
        file = extract_name(user_input) or input("Script name: ")
        return run_script(file)

    return "Unknown automation task"