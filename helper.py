from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceBgeEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings
 
#   EXTRACT THE PDF

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Data")


def load_pdf_files(data):
    try:
        loader=DirectoryLoader(data,
        glob="*.pdf",
        loader_cls=PyPDFLoader)
        documents=loader.load()
        return documents
    except Exception as e:
        print("error",e)


# extracted_data = load_pdf_files(data=DATA_PATH)

extracted_data=load_pdf_files(data=DATA_PATH)


from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_split(extracted_data):
    # Create a text splitter with chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks



# def download_hugging_face_embeddings():
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     return embeddings
