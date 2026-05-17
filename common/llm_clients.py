"""
Common LLM client wrappers for Anthropic Claude and OpenAI
"""
import os
from typing import Optional, List, Dict, Any
from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class ClaudeClient:
    """Wrapper for Anthropic Claude API"""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model or os.getenv("DEFAULT_LLM_MODEL", "claude-sonnet-4-20250514")
        self.client = Anthropic(api_key=self.api_key)
    
    def chat(
        self, 
        messages: List[Dict[str, str]], 
        max_tokens: int = 4096,
        temperature: float = 0.7,
        system: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Send a chat completion request to Claude
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0-1)
            system: Optional system prompt
            
        Returns:
            Assistant's response text
        """
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system if system else None,
            messages=messages,
            **kwargs
        )
        return response.content[0].text
    
    def stream_chat(
        self, 
        messages: List[Dict[str, str]], 
        max_tokens: int = 4096,
        temperature: float = 0.7,
        system: Optional[str] = None,
        **kwargs
    ):
        """
        Stream chat completion from Claude
        
        Yields response chunks as they arrive
        """
        with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system if system else None,
            messages=messages,
            **kwargs
        ) as stream:
            for text in stream.text_stream:
                yield text


class OpenAIClient:
    """Wrapper for OpenAI API (mainly for embeddings)"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.embedding_model = os.getenv("DEFAULT_EMBEDDING_MODEL", "text-embedding-3-small")
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Get embedding vector for text
        
        Args:
            text: Input text to embed
            
        Returns:
            Embedding vector (1536 dimensions for text-embedding-3-small)
        """
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=text
        )
        return response.data[0].embedding
    
    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Get embeddings for multiple texts in one request
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=texts
        )
        return [item.embedding for item in response.data]


# Example usage
if __name__ == "__main__":
    # Test Claude client
    claude = ClaudeClient()
    response = claude.chat([
        {"role": "user", "content": "Hello! What is RAG in AI?"}
    ])
    print("Claude:", response)
    
    # Test OpenAI embeddings
    openai_client = OpenAIClient()
    embedding = openai_client.get_embedding("This is a test sentence")
    print(f"\nEmbedding dimension: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")
