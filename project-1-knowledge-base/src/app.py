"""
Streamlit UI for Personal Knowledge Base
"""
import sys
from pathlib import Path
import streamlit as st

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.query import KnowledgeBase


def main():
    st.set_page_config(
        page_title="Personal Knowledge Base",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 Personal Knowledge Base")
    st.markdown("Ask questions about your documents using RAG!")
    
    # Initialize KB (with caching)
    @st.cache_resource
    def load_kb():
        return KnowledgeBase()
    
    try:
        kb = load_kb()
        num_docs = kb.vector_store.get_count()
        
        st.sidebar.success(f"✓ Loaded {num_docs} chunks")
        
    except Exception as e:
        st.error(f"Error loading knowledge base: {e}")
        st.info("Make sure you've run `python src/ingest.py` first!")
        return
    
    # Settings in sidebar
    st.sidebar.header("⚙️ Settings")
    top_k = st.sidebar.slider("Number of chunks to retrieve", 1, 10, 5)
    show_sources = st.sidebar.checkbox("Show source chunks", value=True)
    
    # Main interface
    st.markdown("---")
    
    # Query input
    question = st.text_input(
        "💬 Ask a question:",
        placeholder="What are the main topics in my documents?",
        key="question_input"
    )
    
    # Submit button
    if st.button("🔍 Search", type="primary") or question:
        if not question:
            st.warning("Please enter a question!")
            return
        
        with st.spinner("Searching knowledge base..."):
            try:
                # Query with sources
                answer, sources = kb.query_with_sources(question, top_k=top_k)
                
                # Display answer
                st.markdown("### 💡 Answer")
                st.markdown(answer)
                
                # Display sources if enabled
                if show_sources and sources:
                    st.markdown("---")
                    st.markdown("### 📚 Source Chunks")
                    
                    for i, source in enumerate(sources, 1):
                        with st.expander(
                            f"Source {i}: {source.metadata.get('source', 'Unknown')} "
                            f"(Score: {source.score:.3f})"
                        ):
                            st.text(source.content)
                            st.caption(f"Metadata: {source.metadata}")
                
            except Exception as e:
                st.error(f"Error: {e}")
    
    # Example questions
    st.markdown("---")
    st.markdown("### 💭 Example Questions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("What are the main topics?"):
            st.session_state.question_input = "What are the main topics covered in these documents?"
            st.rerun()
        
        if st.button("Give me a summary"):
            st.session_state.question_input = "Can you provide a summary of the key points?"
            st.rerun()
    
    with col2:
        if st.button("What are the key findings?"):
            st.session_state.question_input = "What are the most important findings or conclusions?"
            st.rerun()
        
        if st.button("List action items"):
            st.session_state.question_input = "Are there any action items or recommendations mentioned?"
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.caption("Built with Anthropic Claude, OpenAI Embeddings, and ChromaDB")


if __name__ == "__main__":
    main()
