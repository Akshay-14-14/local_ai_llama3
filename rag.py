import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import BASE_DIR, CHUNK_SIZE, TOP_K

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = []
vecs = []

def chunk(text):
    return [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]


def load_docs(folder=os.path.join(BASE_DIR, "data", "docs")):
    # ✅ AUTO CREATE FOLDER
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"📁 Created missing folder: {folder}")
        return None

    files = os.listdir(folder)

    if not files:
        print("⚠️ No documents found for RAG")
        return None

    for f in files:
        path = os.path.join(folder, f)

        if not os.path.isfile(path):
            continue

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

            for c in chunk(text):
                docs.append(c)
                vecs.append(model.encode(c))

    if vecs:
        index = faiss.IndexFlatL2(len(vecs[0]))
        index.add(np.array(vecs))
        return index

    return None


index = load_docs()


def retrieve(q):
    if index is None:
        return []

    v = model.encode(q)
    D, I = index.search(np.array([v]), TOP_K)

    return [docs[i] for i in I[0]]