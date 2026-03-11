from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
#from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import HuggingFacePipeline
#from langchain.chains import RetrievalQA
from langchain_classic.chains import RetrievalQA
from transformers import pipeline

def load_rag(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    generator = pipeline(
        "text-generation",
        model="gpt2",
        max_new_tokens=150
    )

    llm = HuggingFacePipeline(pipeline=generator)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa
