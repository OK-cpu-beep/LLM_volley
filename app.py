"""
Main Streamlit dashboard for Volleyball AI Coach.
Provides RAG question answering and analytics visualization.
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv

from src.rag.retriever import Retriever
from src.rag.generator import RAGGenerator
from src.analytics.volleyball_stats import compute_player_stats, compute_team_stats
from src.analytics.data_loader import load_player_actions

load_dotenv()

# Page config
st.set_page_config(page_title="Volleyball AI Coach", page_icon="🏐", layout="wide")

@st.cache_resource
def load_rag_system():
    """Load RAG retriever and generator (cached)."""
    try:
        retriever = Retriever()
        generator = RAGGenerator()
        return retriever, generator
    except Exception as e:
        st.error(f"Failed to load RAG system: {e}")
        st.info("Make sure you have run `python scripts/ingest_docs.py` first.")
        return None, None

def main():
    st.title("🏐 Volleyball AI Coach")
    st.markdown("*Intelligent training support using RAG + sports analytics*")
    
    retriever, generator = load_rag_system()
    
    tab1, tab2 = st.tabs(["💬 RAG Assistant (Ask anything)", "📊 Analytics Dashboard"])
    
    # ---------- TAB 1: RAG Assistant ----------
    with tab1:
        st.header("Ask about volleyball techniques, tactics, drills")
        
        question = st.text_area("Your question:", height=100,
                                placeholder="e.g., How to improve timing in a spike?")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            top_k = st.slider("Number of retrieved chunks", 1, 10, 3)
        with col2:
            submit = st.button("Get Answer", type="primary")
        
        if submit and question:
            if retriever is None or generator is None:
                st.error("RAG system not available. Please check setup.")
            else:
                with st.spinner("Retrieving relevant knowledge..."):
                    docs = retriever.retrieve(question, top_k=