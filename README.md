# LangChain-Loaders

# LangChain Loaders Practice

This repository contains practice code and experiments with **LangChain document loaders**.  
The goal is to explore how to load different types of documents (PDF, TXT, web pages, etc.) into LangChain for further processing in LLM and RAG workflows.

---

## 📌 Features
- Practice with different **LangChain loaders**:
  - `PyPDFLoader` – Load and extract text from PDF files
  - `TextLoader` – Load plain text files
  - `DirectoryLoader` – Load all files from a directory
  - `UnstructuredURLLoader` – Load text directly from a web page

---

## 🛠️ Requirements
Install dependencies using:

```bash
pip install -r requirements.txt


.
├── loaders/                  # Document loader practice files
│   ├── pdf_loader_practice.py
│   ├── text_loader_demo.py
│   ├── url_loader_demo.py
│   └── directory_loader_demo.py
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation

