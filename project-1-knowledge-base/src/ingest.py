"""
Document ingestion pipeline for Personal Knowledge Base
Loads documents, chunks them, creates embeddings, and stores in vector DB
"""
import os
import sys
from pathlib import Path
from typing import List, Dict, Any
from loguru import logger

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from common.llm_clients import OpenAIClient
from common.vector_store import ChromaDBStore
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentIngester:
    """Handles document loading, chunking, and indexing"""
    
    def __init__(
        self,
        data_dir: str = "./data",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        collection_name: str = "knowledge_base"
    ):
        self.data_dir = Path(data_dir)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize clients
        self.embedding_client = OpenAIClient()
        self.vector_store = ChromaDBStore(collection_name=collection_name)
        
        # Text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        logger.info(f"Initialized ingester with chunk_size={chunk_size}, overlap={chunk_overlap}")
    
    def load_pdf(self, filepath: Path) -> str:
        """Extract text from PDF"""
        try:
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            logger.error(f"Error loading PDF {filepath}: {e}")
            return ""
    
    def load_text(self, filepath: Path) -> str:
        """Load plain text file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error loading text file {filepath}: {e}")
            return ""
    
    def load_document(self, filepath: Path) -> str:
        """Load document based on file extension"""
        ext = filepath.suffix.lower()
        
        if ext == '.pdf':
            return self.load_pdf(filepath)
        elif ext in ['.txt', '.md']:
            return self.load_text(filepath)
        else:
            logger.warning(f"Unsupported file type: {ext}")
            return ""
    
    def chunk_document(self, text: str, source: str) -> List[Dict[str, Any]]:
        """
        Split document into chunks with metadata
        
        Returns:
            List of dicts with 'content' and 'metadata'
        """
        chunks = self.text_splitter.split_text(text)
        
        return [
            {
                "content": chunk,
                "metadata": {
                    "source": source,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                }
            }
            for i, chunk in enumerate(chunks)
        ]
    
    def ingest_directory(self) -> int:
        """
        Process all documents in data directory
        
        Returns:
            Number of chunks ingested
        """
        if not self.data_dir.exists():
            logger.error(f"Data directory not found: {self.data_dir}")
            return 0
        
        # Find all supported files
        files = list(self.data_dir.glob("*.pdf")) + \
                list(self.data_dir.glob("*.txt")) + \
                list(self.data_dir.glob("*.md"))
        
        if not files:
            logger.warning(f"No documents found in {self.data_dir}")
            return 0
        
        logger.info(f"Found {len(files)} document(s) to process")
        
        all_chunks = []
        
        # Process each file
        for filepath in files:
            logger.info(f"Processing: {filepath.name}")
            
            # Load document
            text = self.load_document(filepath)
            if not text:
                continue
            
            # Chunk it
            chunks = self.chunk_document(text, filepath.name)
            all_chunks.extend(chunks)
            
            logger.info(f"  → Created {len(chunks)} chunk(s)")
        
        if not all_chunks:
            logger.error("No chunks created from documents")
            return 0
        
        # Create embeddings (batch for efficiency)
        logger.info(f"Creating embeddings for {len(all_chunks)} chunk(s)...")
        contents = [chunk["content"] for chunk in all_chunks]
        embeddings = self.embedding_client.get_embeddings_batch(contents)
        
        # Store in vector DB
        logger.info("Storing in vector database...")
        self.vector_store.add_documents(
            documents=contents,
            embeddings=embeddings,
            metadata=[chunk["metadata"] for chunk in all_chunks]
        )
        
        logger.success(f"✓ Ingested {len(all_chunks)} chunks from {len(files)} document(s)")
        return len(all_chunks)


def main():
    """Run ingestion pipeline"""
    # Get config from environment
    chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "200"))
    
    # Run ingestion
    ingester = DocumentIngester(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    num_chunks = ingester.ingest_directory()
    
    if num_chunks > 0:
        logger.info(f"Knowledge base ready with {num_chunks} chunks!")
        logger.info("Try: python src/query.py 'your question here'")
    else:
        logger.error("Ingestion failed - add documents to data/ folder")


if __name__ == "__main__":
    main()
