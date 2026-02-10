# George Soros AI Chatbot

A RAG-based chatbot that provides educational insights inspired by George Soros's investment philosophy.

## Features

- 💬 Interactive Streamlit UI with Soros-themed design
- 📚 RAG (Retrieval-Augmented Generation) using ChromaDB
- 🧠 Powered by Google Gemini AI
- 📊 Market data integration via yfinance
- 💡 Educational insights on reflexivity, market psychology, and macro analysis

## Installation

1. Activate your virtual environment:
```bash
venv\Scripts\activate
```

2. Install Streamlit (if not already installed):
```bash
pip install streamlit
```

## Running the Application

### Streamlit UI (Recommended)
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### CLI Version
```bash
python chat_cli.py
```

## Usage

Simply type your questions about:
- Trading strategies
- Investment philosophy
- Market analysis
- Soros's concepts (reflexivity, feedback loops, etc.)
- Specific tickers (e.g., "What would Soros think about TSLA?")

**Note:** This chatbot provides educational content only and is NOT financial advice.

## Project Structure

- `app.py` - Streamlit UI application
- `chat_cli.py` - Command-line interface
- `rag_interface.py` - Main RAG chatbot logic
- `rag_retriever.py` - ChromaDB retrieval system
- `rag_generator.py` - Gemini answer generation
- `ticker_utils.py` - Ticker extraction utilities
- `market_data.py` - Market data fetching
- `data/Soros_Questions.xlsx` - Knowledge base
