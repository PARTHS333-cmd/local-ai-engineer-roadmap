from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="../phase_4_rag/chroma_db",
    embedding_function=embedding
)

def search_resume(query):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )