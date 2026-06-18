import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

class RAGPipeline:
    """
    Handles PDF ingestion, embedding, and retrieval using ChromaDB.
    """
    
    def __init__(self, db_dir="data/chroma_db", kb_dir="knowledge_base"):
        self.db_dir = db_dir
        self.kb_dir = kb_dir
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = None
        
        # Initialize knowledge base directory
        if not os.path.exists(self.kb_dir):
            os.makedirs(self.kb_dir)
            
        self._load_or_create_db()

    def _load_or_create_db(self):
        if os.path.exists(self.db_dir) and len(os.listdir(self.db_dir)) > 0:
            self.vector_store = Chroma(persist_directory=self.db_dir, embedding_function=self.embeddings)
        else:
            self.rebuild_index()

    def rebuild_index(self):
        """Indexes all PDFs in the knowledge_base folder."""
        if not os.path.exists(self.kb_dir) or len(os.listdir(self.kb_dir)) == 0:
            print("Knowledge base is empty. Please add PDFs.")
            return

        loader = DirectoryLoader(self.kb_dir, glob="./*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        
        if not documents:
            return

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(documents)
        
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.db_dir
        )

    def get_retriever(self):
        if self.vector_store:
            return self.vector_store.as_retriever(search_kwargs={"k": 3})
        return None

    def query(self, user_query, ai_client):
        """Combines retrieval with LLM response."""
        retriever = self.get_retriever()
        if not retriever:
            return ai_client.get_response(user_query)
            
        # Get relevant context
        docs = retriever.get_relevant_documents(user_query)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        prompt = f"""
        Context from Sustainability Guides:
        {context}
        
        User Query: {user_query}
        
        Please provide a helpful, actionable response based on the context above. 
        If the context doesn't contain the answer, use your general knowledge but specify that.
        """
        
        return ai_client.get_response(prompt)
