import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from config import FILE,LLM

# DocumentLoader loads a document from the given file_path using PyPDFLoader.
class DocumentLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Load the document from the given file path.

        Returns:
            list: List of pages in the document.
        """
        loader = PyPDFLoader(self.file_path)
        return loader.load()

# DocumentSplitter splits a document into smaller chunks based on the provided chunk_size and chunk_overlap.
class DocumentSplitter:
    def __init__(self, chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_document(self, document):
        """Split the given document into smaller chunks.

        Args:
            document (str): The document content as a single string.

        Returns:
            list: List of smaller documents (chunks).
        """
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        return splitter.create_documents(document)

# VectorDatabase creates a vector database from the given embeddings and documents.
class VectorDatabase:
    def __init__(self, embeddings):
        self.embeddings = embeddings

    def create_from_documents(self, documents):
        """Create a vector database (Chroma) from the given list of documents.

        Args:
            documents (list): List of documents (strings).

        Returns:
            Chroma: A vector database created from the documents using the provided embeddings.
        """
        return Chroma.from_documents(documents, self.embeddings)

# DocumentRetriever retrieves similar documents from the vector database.
class DocumentRetriever:
    def __init__(self, db, k):
        self.db = db
        self.k = k

    def retriever(self):
        """Create a retriever using the vector database.

        Returns:
            RetrievalQA: A retriever for searching similar documents based on embeddings.
        """
        return self.db.as_retriever(search_type="similarity", search_kwargs={"k": self.k})

# Chatbot represents a chatbot instance using the specified language model, memory, and retriever.
class Chatbot:
    def __init__(self, llm_name, temperature, memory, retriever):
        self.llm_name = llm_name
        self.temperature = temperature
        self.memory = memory
        self.retriever = retriever

    def create_chatbot_chain(self):
        """Create a conversational retrieval chain using the specified components.

        Returns:
            ConversationalRetrievalChain: A chain combining the language model, memory, and retriever.
        """
        return ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model_name=self.llm_name, temperature=self.temperature),
            chain_type="stuff",
            memory=self.memory,
            retriever=self.retriever,
            verbose=True,
        )

# ChatbotSystem manages the entire chatbot system, including loading the document, creating a chatbot, and handling chat queries.
class ChatbotSystem:
    def __init__(self, file_path, llm_name, temperature, chunk_size, chunk_overlap, k):
        self.document_loader = DocumentLoader(file_path)
        self.document_splitter = DocumentSplitter(chunk_size, chunk_overlap)
        self.vector_db = None
        self.retriever = None
        self.chatbot = Chatbot(llm_name, temperature, ConversationBufferMemory(memory_key="chat_history", return_messages=True), None)
        self.k = k

    def load_db(self):
        """Load the document, split it into chunks, and create the vector database and retriever."""
        pages = self.document_loader.load()
        page = [pages[85].page_content]
        docs = self.document_splitter.split_document(page)
        embeddings = OpenAIEmbeddings()
        self.vector_db = VectorDatabase(embeddings)
        self.chroma_db = self.vector_db.create_from_documents(docs)
        self.retriever = DocumentRetriever(self.chroma_db, self.k).retriever()
        self.chatbot.retriever = self.retriever

    def chat(self, question):
        """Chat with the chatbot using the given question.

        Args:
            question (str): The user's question/query.

        Returns:
            str: The chatbot's response to the question.
        Raises:
            ValueError: If the database is not loaded. Call 'load_db()' before using chatbot.
        """
        if not self.retriever:
            raise ValueError("Database not loaded. Call 'load_db()' before using chatbot.")
        response = self.chatbot.create_chatbot_chain()({"question": question})
        return response['answer']

# Example usage:
# if __name__ == "__main__":
#     chatbot_system = ChatbotSystem(
#         file_path=FILE,
#         llm_name=LLM,
#         temperature=0,
#         chunk_size=2000,
#         chunk_overlap=200,
#         k=4
#     )
#     chatbot_system.load_db()
#     question = "What are the symptoms of breast cancer?"
#     answer = chatbot_system.chat(question)
#     print(answer)
