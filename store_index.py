from src.helper import load_pdf_files, text_split
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceEmbeddings


#  LOAD ENV 
load_dotenv()
PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY

extracted_data=load_pdf_files(data="Data/")
text_chunks=text_split(extracted_data)
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "keralatravelbot"

pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )


docssearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)


