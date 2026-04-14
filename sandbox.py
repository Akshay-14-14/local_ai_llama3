import os
import shutil
import subprocess
from config import WORKSPACE

import os
from config import WORKSPACE

def safe_path(path):
    # ✅ Normalize workspace
    workspace = os.path.abspath(WORKSPACE)

    # ✅ Join and normalize user path
    full_path = os.path.abspath(os.path.join(workspace, path))

    # ✅ Debug (optional)
    # print("Workspace:", workspace)
    # print("Full Path:", full_path)

    # ✅ Proper check (IMPORTANT)
    if not full_path.startswith(workspace + os.sep):
        raise Exception("❌ خارج sandbox")

    return full_path


def confirm(msg):
    print(f"⚠️ {msg}")
    return input("Type YES: ").lower() == "yes"

def create_folder(name):
    path = safe_path(name)
    os.makedirs(path, exist_ok=True)
    return f"📁 Folder created: {name}"

def create_file(name):
    if not confirm(f"Create file {name}?"):
        return "Cancelled"
    path = safe_path(name)
    open(path, "w").close()
    return f"✅ Created {name}"

def delete_folder(name):
    path = safe_path(name)

    if not os.path.exists(path):
        return f"❌ Folder not found: {name}"

    if not os.path.isdir(path):
        return f"❌ Not a folder: {name}"

    if not confirm(f"Delete folder '{name}' and ALL its contents?"):
        return "Cancelled"

    shutil.rmtree(path)
    return f"🗑 Folder deleted: {name}"

def delete_file(name):
    if not confirm(f"Delete {name}?"):
        return "Cancelled"
    os.remove(safe_path(name))
    return f"🗑 Deleted {name}"


def list_files():
    return os.listdir(WORKSPACE)


def run_script(file):
    if not confirm(f"Run script {file}?"):
        return "Cancelled"
    result = subprocess.run(
        ["python", safe_path(file)],
        capture_output=True,
        text=True,
        encoding="utf-8", 
        errors="ignore"
    )
    return result.stdout or result.stderr