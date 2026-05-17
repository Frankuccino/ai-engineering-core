"""
RAG Query Engine for Knowledge Base
Handles semantic search and answer generation
"""
import sys
from pathlib import Path
from typing import List, Tuple, Optional
from loguru import logger

sys.path.append(str(Path(__file__).parent.parent.parent))

from common.llm_clients import ClaudeClient, OpenAIClient
from common.vector_store import ChromaDBStore, SearchResult


class KnowledgeBase:
    """RAG-powered knowledge base for Q&A"""
    
    def __init__(
        self,
        collection_name: str = "knowledge_base",
        top_k: int = 5
    ):
        self.collection_name = collection_name
        self.top_k = top_k
        
        # Initialize clients
        self.claude = ClaudeClient()
        self.embedding_client = OpenAIClient()
        self.vector_store = ChromaDBStore(collection_name=collection_name)
        
        logger.info(f"Initialized KB with {self.vector_store.get_count()} chunks")
    
    def query(
        self,
        question: str,
        top_k: Optional[int] = None
    ) -> str:
        """
        Query the knowledge base
        
        Args:
            question: User's question
            top_k: Number of chunks to retrieve (default: self.top_k)
            
        Returns:
            Generated answer
        """
        k = top_k or self.top_k
        
        # Get query embedding
        query_embedding = self.embedding_client.get_embedding(question)
        
        # Search vector store
        results = self.vector_store.search(query_embedding, top_k=k)
        
        if not results:
            return "I don't have enough information to answer that question."
        
        # Build context from results
        context = self._build_context(results)
        
        # Generate answer
        answer = self._generate_answer(question, context)
        
        return answer
    
    def query_with_sources(
        self,
        question: str,
        top_k: Optional[int] = None
    ) -> Tuple[str, List[SearchResult]]:
        """
        Query with source citations
        
        Returns:
            Tuple of (answer, list of source chunks)
        """
        k = top_k or self.top_k
        
        # Get query embedding
        query_embedding = self.embedding_client.get_embedding(question)
        
        # Search vector store
        results = self.vector_store.search(query_embedding, top_k=k)
        
        if not results:
            return "I don't have enough information to answer that question.", []
        
        # Build context
        context = self._build_context(results)
        
        # Generate answer
        answer = self._generate_answer(question, context, include_sources=True)
        
        return answer, results
    
    def _build_context(self, results: List[SearchResult]) -> str:
        """Build context string from search results"""
        context_parts = []
        
        for i, result in enumerate(results, 1):
            source = result.metadata.get('source', 'Unknown')
            context_parts.append(
                f"[Source {i}: {source}]\n{result.content}\n"
            )
        
        return "\n".join(context_parts)
    
    def _generate_answer(
        self,
        question: str,
        context: str,
        include_sources: bool = False
    ) -> str:
        """Generate answer using Claude"""
        
        system_prompt = """You are a helpful assistant that answers questions based on the provided context.

Rules:
- Only use information from the context provided
- If the context doesn't contain the answer, say "I don't have enough information to answer that"
- Be concise but complete
- Cite sources when relevant using [Source X] notation"""

        user_prompt = f"""Context from documents:

{context}

Question: {question}

Answer the question based only on the context above."""

        if include_sources:
            user_prompt += "\n\nInclude [Source X] citations in your answer."
        
        answer = self.claude.chat(
            messages=[{"role": "user", "content": user_prompt}],
            system=system_prompt,
            temperature=0.3  # Lower temperature for factual answers
        )
        
        return answer


def main():
    """CLI interface for querying knowledge base"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python query.py 'your question here'")
        print("\nExample: python query.py 'What are the main topics in my documents?'")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    
    try:
        kb = KnowledgeBase()
        
        print(f"\n🔍 Question: {question}\n")
        print("⏳ Searching knowledge base...")
        
        answer, sources = kb.query_with_sources(question)
        
        print(f"\n💡 Answer:\n{answer}\n")
        
        print("📚 Sources:")
        for i, source in enumerate(sources, 1):
            print(f"  [{i}] {source.metadata.get('source', 'Unknown')} (score: {source.score:.3f})")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        print(f"\n❌ Error: {e}")
        print("\nMake sure you've run 'python src/ingest.py' first!")


if __name__ == "__main__":
    main()
