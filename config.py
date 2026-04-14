import os

BASE_DIR = "D:/local_ai"

WORKSPACE = os.path.abspath(os.path.join(BASE_DIR, "workspace"))

MODEL = "llama3"

ENABLE_INTERNET = False

CHUNK_SIZE = 300
TOP_K = 3