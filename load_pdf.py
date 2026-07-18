from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 1 — Load PDF
loader = PyPDFLoader("docs/gauriid_resume.pdf")  # change filename
pages = loader.load()

print(f"Total pages loaded: {len(pages)}")
print(f"First page preview: {pages[0].page_content[:200]}")

# Step 2 — Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(pages)

print(f"Total chunks created: {len(chunks)}")
print(f"First chunk: {chunks[0].page_content}")