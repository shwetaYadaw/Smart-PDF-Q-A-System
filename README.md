# Smart-PDF-Q-A-System

Project Overview

This project is a Smart PDF Question and Answer System that allows users to upload a PDF document and ask questions related to its content. The system reads the document, understands the information, and provides relevant answers based on the user’s query.

The main goal of this project is to reduce the time required to manually search through long documents and make information retrieval faster and easier.

Features
Upload and read PDF documents
Automatically extract and process text
Ask questions related to the document
Get accurate answers from the content
Works on large documents efficiently
Technologies Used
Python

Python is used as the main programming language because it is simple and widely used for AI-based applications.

LangChain

LangChain is used to connect different parts of the system such as document loading, text processing, and interaction with the language model.

FAISS

FAISS is used as a vector database to store and search document data efficiently. It helps in finding the most relevant content quickly.

Sentence Transformers

This is used to convert text into numerical form (embeddings) so that the system can understand and compare the meaning of text.

Transformers (Hugging Face)

This library provides pre-trained language models which are used to generate answers based on the document content.

FLAN-T5 Model

This is the language model used to generate answers. It is lightweight and works efficiently on normal systems.

PyPDF

This library is used to read and extract text from PDF files.

How It Works
The system loads the PDF file and extracts the text.
The text is divided into smaller parts for better processing.
Each part is converted into embeddings (numerical representation).
These embeddings are stored in FAISS for fast searching.
When a user asks a question, the system finds the most relevant part of the document.
The selected content is passed to the language model.
The model generates and returns the final answer.
Installation

Install the required libraries using the following command:

pip install langchain langchain-community langchain-text-splitters langchain-huggingface faiss-cpu transformers sentence-transformers pypdf
Usage
Place your PDF file in the project folder.
Update the file path in the code.
Run the Python script.
Enter your question in the terminal.
The system will return the answer based on the document.
Example

If a user uploads a document and asks:
“What is web analytics?”

The system will search the document and return the relevant answer without requiring the user to read the entire file.

Advantages
Saves time
Easy to use
Works on large documents
No need to manually search content
Limitations
Depends on the quality of the PDF content
May not give perfect answers for very complex queries
Requires internet for downloading models initially
Future Improvements
Add a user interface using Streamlit
Support multiple PDF files
Improve answer accuracy using advanced models
Add voice-based query system
Conclusion

This project demonstrates how AI and language models can be used to simplify document search and improve user experience. It is useful for students, researchers, and professionals who work with large documents.
