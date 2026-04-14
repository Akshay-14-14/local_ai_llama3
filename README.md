# 🤖 Local AI Assistant (Offline + Sandbox + Multi-Adapter)

A fully offline, privacy-focused AI assistant powered by a local LLM (**Llama3 8B**) with modular adapters, RAG (Retrieval-Augmented Generation), and a secure sandbox execution environment.

---

## 🚀 Features

* 🔒 **100% Offline & Private** – No data leaves your system
* 🧠 **Local LLM (Llama3 8B)** via Ollama
* 🧩 **Multi-Adapter Architecture**

  * Coding Assistant
  * Automation Agent
  * Tamil Language Support
  * Study Assistant
* 📚 **RAG System (FAISS + Embeddings)** for contextual answers
* 🛡 **Sandbox Execution**

  * Safe file/folder operations
  * Script execution with confirmation
* 💾 **Memory System (SQLite)** – Stores conversation history
* 🧭 **Hybrid Router**

  * Rule-based + LLM classification
* ⚙️ **Command Execution**

  * Create/Delete/List files & folders
  * Run Python scripts safely

---

## 🏗 Architecture Overview

```
User Input
   ↓
Router (Rule + LLM)
   ↓
RAG (Context Retrieval)
   ↓
Adapter चयन
   ↓
Sandbox Execution / LLM Response
   ↓
Memory Storage (SQLite)
```

---

## 📁 Project Structure

```
local_ai/
│
├── adapters/
│   ├── coding.py
│   ├── automation.py
│   ├── tamil.py
│   └── study.py
│
├── data/
│   ├── docs/        # RAG documents
│   └── db.sqlite    # Memory database
│
├── workspace/       # Sandbox directory
│
├── main.py          # Entry point
├── router.py        # Task routing logic
├── rag.py           # RAG system (FAISS)
├── sandbox.py       # Secure execution layer
├── llm.py           # LLM interface (Ollama)
├── memory.py        # Chat storage
└── config.py        # Configurations
```

---

## ⚙️ Installation

### 1️⃣ Install Ollama

Download from: https://ollama.com

```bash
ollama pull llama3
```

---

### 2️⃣ Install Python Dependencies

```bash
pip install faiss-cpu sentence-transformers numpy
```

---

### 3️⃣ Setup Project

```bash
git clone <your-repo-url>
cd local_ai
mkdir workspace
mkdir data/docs
```

---

## ▶️ Usage

```bash
cd D:\local_ai
chcp 65001
python main.py
```

---

## 🧪 Example Commands

### 📂 File & Folder Operations

```
create folder test
delete folder test
create file app.py
list
```

### 🧠 AI Queries

```
what is java?
explain cloud computing
```

### 💻 Coding

```
write python code for fibonacci
```

### 🌐 Tamil Support

```
explain AI in tamil
```

---

## 🔒 Security Model

* All operations are restricted to the **workspace/** directory
* Path validation prevents directory traversal attacks
* User confirmation required for:

  * File creation
  * Deletion
  * Script execution

---

## 📚 RAG (Retrieval-Augmented Generation)

* Uses **FAISS** for vector search
* Embeddings via **sentence-transformers**
* Supports:

  * Document chunking
  * Context retrieval
  * Local knowledge base

---

## ⚡ Advantages

* Full privacy (offline AI)
* No API cost
* Highly customizable
* System-level automation capability

---

## ⚠️ Limitations

* No real-time internet data
* Slower than cloud-based models
* Requires local compute resources

---

## 🚀 Future Improvements

* 🤖 Auto-Agent (multi-step execution)
* 🧠 Smart memory (semantic recall)
* 🎤 Voice assistant (offline)
* 🖥 GUI interface
* 🌐 Optional internet mode (toggle-based)
* 🔁 Self-healing code execution

---

## 👨‍💻 Author

**Akshay. S**
Aspiring Cloud & DevOps Developer

---

## ⭐ Contribute

Pull requests are welcome!
Feel free to improve adapters, routing, or UI.

---

## 📜 License

This project is open-source and available under the MIT License.
