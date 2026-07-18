from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Load vector DB
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Load LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

def ask(question):
    # Step 1 — Retrieve relevant chunks
    chunks = vectordb.similarity_search(question, k=3)
    context = "\n\n".join([chunk.page_content for chunk in chunks])
    
    # Step 2 — Generate answer using context
    prompt = f"""Answer the question using only the context below.
If the answer is not in the context, say "I don't know based on the document."

Context:
{context}

Question: {question}
Answer:"""
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    print(f"\nQ: {question}")
    print(f"A: {response.content}")
    print("---")

# Test with your PDF
ask("What is this document about?")
ask("What are the main topics covered?")
ask("Summarize the key points")

print("\n=== Chat with your PDF ===")
print("Type 'quit' to exit\n")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        print("Goodbye!")
        break
    if question.strip() == "":
        continue
    ask(question)