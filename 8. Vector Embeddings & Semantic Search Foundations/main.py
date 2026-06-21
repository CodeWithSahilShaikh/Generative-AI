from dotenv import load_dotenv
load_dotenv()
import os
# ab inn vectors ko store krwane ke liye hme vector database ki jarurat h.

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

# 1. Initialize your embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

# 2. Get the index name from your project configuration
index_name = "py-index"

# 3. Connect to Pinecone using the official LangChain initialization method
# Note: Ensure you have PINECONE_API_KEY set in your .env file
vector_store = PineconeVectorStore.from_existing_index(
    index_name=index_name, 
    embedding=embeddings
)

# 4. Add your data and print the resulting vector IDs
print(vector_store.add_texts(["ring"]))