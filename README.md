# Volleyball AI Coach — RAG-based Intelligent Training Support System

An intelligent system that combines **Large Language Models (LLM)**, **sports analytics**, and **Retrieval-Augmented Generation (RAG)** to assist volleyball coaches and players.  
It answers questions about techniques, tactics, and drills using a curated knowledge base, and provides performance analytics from match logs.

## ✨ Features
- **RAG Chatbot** – Ask anything about volleyball training (e.g., “How to improve jump float serve?”) and get context‑aware answers using OpenAI + your knowledge base.
- **Vector Search** – Embeddings from `sentence-transformers/all-MiniLM-L6-v2`, stored in FAISS for fast retrieval.
- **Analytics Module** – Compute key performance indicators: attack efficiency, serve success rate, passing accuracy, etc.
- **Interactive Dashboard** – Built with Streamlit: two tabs for Q&A and player stats visualisation.

## 🧠 How RAG Works in This Project
1. Documents (text files in `data/knowledge/`) are split into chunks.
2. Each chunk is embedded and stored in a FAISS index.
3. User’s question is embedded and the top‑k relevant chunks are retrieved.
4. Retrieved context + the question are sent to an LLM (OpenAI GPT‑3.5‑Turbo) to generate an answer.
5. Answer is shown together with source references.

## 📦 Tech Stack
- Python 3.9+
- Streamlit – UI
- OpenAI API – LLM (can be replaced with any OpenAI‑compatible endpoint)
- Sentence‑Transformers – embeddings
- FAISS – vector database
- Pandas / Plotly – analytics and charts

## ⚙️ Setup

### 1. Clone & install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-key-here
```

Or set it as an environment variable.

### 3. Ingest knowledge base (build FAISS index)

```
python scripts/ingest_docs.py
```

This will create a `faiss_index` folder with the vector store.

### 4. Run the Streamlit app

```
streamlit run app.py
```

## 📁 Project Structure

```
.
├── app.py                     # Main Streamlit dashboard
├── requirements.txt
├── .env.example
├── README.md
├── scripts/
│   └── ingest_docs.py         # One‑time script to index knowledge
├── src/
│   ├── rag/
│   │   ├── embedding.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── generator.py
│   ├── analytics/
│   │   ├── volleyball_stats.py
│   │   └── data_loader.py
│   └── knowledge_base/
│       └── document_processor.py
└── data/
    ├── knowledge/             # Add your own .txt files here
    └── player_stats/
        └── sample_matches.csv
```

## 📊 Example Questions for the RAG Assistant

- “What are the key phases of a volleyball spike?”
- “How to run a 6‑2 offensive system?”
- “Give me 3 drills to improve passing under pressure.”

## 📈 Analytics Demo

Upload a CSV with columns: `player`, `action` (serve, attack, pass, block, etc.), `result` (success, error, etc.), `timestamp`.
The system calculates:

- Attack efficiency = (kills - errors) / total attacks
- Serve success rate
- Passing rating (3‑point scale)

## 🔧 Customisation

- **Add more knowledge**: put any `.txt` file into `data/knowledge/` and re‑run `ingest_docs.py`.
- **Switch LLM**: modify `src/rag/generator.py` to use a local model (e.g., HuggingFace pipeline) or a different API.
- **Change embedding model**: edit `EMBEDDING_MODEL_NAME` in `src/rag/embedding.py`.

## 📝 License

MIT – free for educational and research use.