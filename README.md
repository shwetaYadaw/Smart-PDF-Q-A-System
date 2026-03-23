# Smart PDF Q&A System

## Project Overview
This project is a Smart PDF Question and Answer System that allows users to upload a PDF document and ask questions related to its content. The system reads the document, understands the information, and provides relevant answers based on the user’s query.

The main goal of this project is to reduce the time required to manually search through long documents and make information retrieval faster and easier.

---

## Features
- Upload and read PDF documents  
- Automatically extract and process text  
- Ask questions related to the document  
- Get accurate answers from the content  
- Works on large documents efficiently  

---

## Technologies Used

### Python
Python is used as the main programming language because it is simple and widely used for AI-based applications.

### LangChain
LangChain is used to connect different parts of the system such as document loading, text processing, and interaction with the language model.

### FAISS
FAISS is used as a vector database to store and search document data efficiently. It helps in finding the most relevant content quickly.

### Sentence Transformers
This is used to convert text into numerical form (embeddings) so that the system can understand and compare the meaning of text.

### Transformers (Hugging Face)
This library provides pre-trained language models which are used to generate answers based on the document content.

### FLAN-T5 Model
This is the language model used to generate answers. It is lightweight and works efficiently on normal systems.

### PyPDF
This library is used to read and extract text from PDF files.

---

## How It Works

1. The system loads the PDF file and extracts the text.  
2. The text is divided into smaller parts for better processing.  
3. Each part is converted into embeddings (numerical representation).  
4. These embeddings are stored in FAISS for fast searching.  
5. When a user asks a question, the system finds the most relevant part of the document.  
6. The selected content is passed to the language model.  
7. The model generates and returns the final answer.  

---

## Installation

Install the required libraries using the following command:

```bash
pip install langchain langchain-community langchain-text-splitters langchain-huggingface faiss-cpu transformers sentence-transformers pypdf
