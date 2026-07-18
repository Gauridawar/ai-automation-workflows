from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Load existing vector database
embeddings = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Search for relevant chunks
def search_docs(question, k=3):
    results = vectordb.similarity_search(question, k=k)
    print(f"\nQuestion: {question}")
    print(f"Found {len(results)} relevant chunks:\n")
    for i, doc in enumerate(results):
        print(f"Chunk {i+1}:")
        print(doc.page_content)
        print("---")
    return results

# Test with questions about your PDF
search_docs("what is this document about?")
search_docs("summarize the main points")