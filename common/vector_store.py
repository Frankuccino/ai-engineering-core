"""
Vector store utilities for ChromaDB, Qdrant, and Pinecone
Start with ChromaDB (simplest), then scale to others as needed
"""
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import chromadb
from chromadb.config import Settings


@dataclass
class SearchResult:
    """Standard search result format"""
    id: str
    content: str
    metadata: Dict[str, Any]
    score: float


class ChromaDBStore:
    """
    ChromaDB vector store - great for local development
    No server required, persists to disk
    """
    
    def __init__(
        self, 
        collection_name: str = "default",
        persist_directory: Optional[str] = None
    ):
        self.collection_name = collection_name
        self.persist_directory = persist_directory or os.getenv(
            "CHROMA_PERSIST_DIRECTORY", 
            "./chroma_db"
        )
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(path=self.persist_directory)
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}  # Use cosine similarity
        )
    
    def add_documents(
        self,
        documents: List[str],
        embeddings: List[List[float]],
        metadata: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None
    ):
        """
        Add documents with their embeddings to the collection
        
        Args:
            documents: List of text documents
            embeddings: List of embedding vectors
            metadata: Optional metadata for each document
            ids: Optional custom IDs (auto-generated if not provided)
        """
        if ids is None:
            # Generate IDs
            ids = [f"doc_{i}" for i in range(len(documents))]
        
        if metadata is None:
            metadata = [{} for _ in documents]
        
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadata,
            ids=ids
        )
    
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        where: Optional[Dict[str, Any]] = None
    ) -> List[SearchResult]:
        """
        Search for similar documents
        
        Args:
            query_embedding: Query vector
            top_k: Number of results to return
            where: Optional metadata filter
            
        Returns:
            List of SearchResult objects
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where
        )
        
        # Convert to SearchResult objects
        search_results = []
        for i in range(len(results['ids'][0])):
            search_results.append(SearchResult(
                id=results['ids'][0][i],
                content=results['documents'][0][i],
                metadata=results['metadatas'][0][i],
                score=1 - results['distances'][0][i]  # Convert distance to similarity
            ))
        
        return search_results
    
    def delete_collection(self):
        """Delete the entire collection"""
        self.client.delete_collection(name=self.collection_name)
    
    def get_count(self) -> int:
        """Get number of documents in collection"""
        return self.collection.count()


# Placeholder for other vector stores - implement when needed

class QdrantStore:
    """Qdrant vector store - production-ready with filtering"""
    
    def __init__(self, collection_name: str = "default"):
        # TODO: Implement when moving to production
        raise NotImplementedError("Qdrant store coming soon!")


class PineconeStore:
    """Pinecone vector store - managed service"""
    
    def __init__(self, index_name: str = "default"):
        # TODO: Implement when scaling up
        raise NotImplementedError("Pinecone store coming soon!")


# Example usage
if __name__ == "__main__":
    from common.llm_clients import OpenAIClient
    
    # Initialize
    vector_store = ChromaDBStore(collection_name="test")
    embedding_client = OpenAIClient()
    
    # Add some documents
    docs = [
        "The quick brown fox jumps over the lazy dog",
        "Machine learning is a subset of artificial intelligence",
        "Python is a popular programming language for AI"
    ]
    
    embeddings = embedding_client.get_embeddings_batch(docs)
    vector_store.add_documents(
        documents=docs,
        embeddings=embeddings,
        metadata=[{"source": f"doc_{i}"} for i in range(len(docs))]
    )
    
    # Search
    query = "Tell me about artificial intelligence"
    query_embedding = embedding_client.get_embedding(query)
    results = vector_store.search(query_embedding, top_k=2)
    
    print(f"Query: {query}\n")
    for i, result in enumerate(results, 1):
        print(f"Result {i} (score: {result.score:.3f}):")
        print(f"  {result.content}\n")
    
    # Cleanup
    vector_store.delete_collection()
