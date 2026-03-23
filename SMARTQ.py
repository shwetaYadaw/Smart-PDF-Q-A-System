from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# Load PDF
loader = PyPDFLoader("C:/Users/HP/Desktop/MKTLATCA1.pdf")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in FAISS
db = FAISS.from_documents(docs, embeddings)

# Load LLM (USE SMALL MODEL)
llm = pipeline("text-generation", model="google/flan-t5-small")

# Chat loop
while True:
    query = input("Ask a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    results = db.similarity_search(query)
    context = results[0].page_content

    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"

    response = llm(prompt, max_length=200)

    print("Answer:", response[0]['generated_text'])