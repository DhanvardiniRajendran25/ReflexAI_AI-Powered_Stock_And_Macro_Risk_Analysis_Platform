# Soros Insights - Backend API

## Overview

This Django project serves as the backend API for a Soros-inspired macro and risk-focused financial analyzer. It provides endpoints to:

1.  Fetch annual financial statement data (Income Statement, Balance Sheet, Cash Flow) for publicly traded companies using the `yfinance` library.
2.  Calculate and return Soros-style risk checks (liquidity, leverage, profitability resilience).
3.  Offer an AI chatbot interface powered by Google's Gemini model, instructed to respond in the style and philosophy of George Soros.
4.  Offer an alternative chatbot interface powered by a custom RAG (Retrieval-Augmented Generation) model, which now mirrors the standalone Streamlit bot: ChromaDB + sentence-transformer embeddings for retrieval and Gemini for generation with ticker-aware market snapshots.

## Features

- **Financial Data Endpoint:** Retrieves statements and calculated Soros-style risk checks for a given stock symbol.
- **Gemini Chatbot Endpoint:** Provides AI-generated responses in Soros's voice via Gemini.
- **RAG Chatbot Endpoint:** Provides AI-generated responses sourced from a Soros-focused Q&A corpus using ChromaDB + sentence-transformer embeddings and Gemini generation (with optional ticker market snapshots).
- **CORS Enabled:** Configured to allow requests from the frontend application.

## Technology Stack

- Python (3.9+ Recommended)
- Django & Django REST Framework
- `yfinance`: For fetching stock financial data.
- `pandas`, `numpy`: For data manipulation.
- `google-generativeai`: For interacting with the Gemini API.
- `transformers`, `torch`, `scikit-learn`: For the RAG pipeline (T5 model and TF-IDF).
- `django-cors-headers`: For handling Cross-Origin Resource Sharing.

## Prerequisites

- Python (3.9 or higher recommended)
- `pip` (Python package installer)
- `virtualenv` or Python's built-in `venv` (Recommended)
- Git

## Setup Instructions

1.  **Clone the Repository**

    ```bash
    git clone [your-repo-url] # Replace with your repository URL
    cd buffet-backend
    ```

2.  **Create/Activate Virtual Environment**

    - _Standard Method:_
      ```bash
      python -m venv venv
      source venv/bin/activate  # macOS/Linux
      # venv\Scripts\activate  # Windows
      ```
    - _External Method (If applicable):_
      Activate your existing shared virtual environment using the appropriate path.
      ```bash
      source /path/to/your/shared/venv/bin/activate
      ```

3.  **Set Up API Key**

    - Obtain a Gemini API Key from [Google AI Studio](https://aistudio.google.com/).
    - Create a file named `secrets.py` in the project root (`buffet-backend/`).
    - Add your API key to this file:
      ```python
      # buffet-backend/secrets.py
      GEMINI_API_KEY = "YOUR_API_KEY_HERE"
      ```
    - **IMPORTANT:** Add `secrets.py` to your `.gitignore` file to avoid committing your key!

4.  **Set Up RAG Corpus**

    - Ensure the `financials_api/data/` directory exists.
    - Place your Question & Answer corpus file inside this directory.
    - **IMPORTANT:** The file _must_ be named `qa_corpus.csv` and be in the format `Question,"Answer"` per line (use CSV quoting if answers contain commas).

5.  **Install Dependencies**

    - Ensure your virtual environment is activated.
    - Generate/update `requirements.txt` if needed: `pip freeze > requirements.txt`
    - Install packages:
      ```bash
      pip install -r requirements.txt
      # Or using specific venv pip:
      # /path/to/your/shared/venv/bin/pip install -r requirements.txt
      ```
      _(Note: Installing PyTorch (`torch`) might require specific commands depending on your OS/CUDA setup. Refer to [PyTorch installation instructions](https://pytorch.org/get-started/locally/) if the standard pip install fails.)_

6.  **Apply Migrations**

    ```bash
    python manage.py migrate
    # Or using specific venv python:
    # /path/to/your/shared/venv/bin/python manage.py migrate
    ```

7.  **Configure CORS**

    - Ensure `django-cors-headers` is installed (should be in `requirements.txt`).
    - Verify `settings.py`:
      - Add `'corsheaders'` to `INSTALLED_APPS`.
      - Add `'corsheaders.middleware.CorsMiddleware'` **at the beginning** of `MIDDLEWARE`.
      - Set `CORS_ALLOWED_ORIGINS` to include your frontend development server URL (e.g., `["http://localhost:5173", "http://127.0.0.1:5173"]`) or set `CORS_ALLOW_ALL_ORIGINS = True` for development (less secure).

8.  **Run the Development Server**
    ```bash
    python manage.py runserver
    # Or using specific venv python:
    # /path/to/your/shared/venv/bin/python manage.py runserver
    ```
    The API should now be running, typically at `http://127.0.0.1:8000/`. The T5 model for the RAG endpoint will be loaded on startup, which might take a few moments.

## API Endpoints

- **`GET /api/financials/<stock_symbol>/`**
  - Retrieves financials and calculated Soros-style risk checks for the given stock symbol.
  - Example: `/api/financials/AAPL/`
- **`POST /api/chatbot/`**
  - Sends a message to the Gemini model (instructed to respond like George Soros).
  - Request Body: `{ "message": "Your question here" }`
  - Response Body: `{ "reply": "Gemini's response here" }`
- **`POST /api/ragbot/`**
  - Sends a message to the custom RAG pipeline (ChromaDB embedding retrieval from Soros Q&A Excel + Gemini generation, optionally enriched with a ticker market snapshot).
  - Request Body: `{ "message": "Your question here" }`
  - Response Body: `{ "reply": "RAG model's response here" }`

### RAG configuration notes
- Place `Soros_Questions.xlsx` in the repo root (used to build the Chroma index automatically).
- Set `GOOGLE_API_KEY` or `GEMINI_API_KEY` (or define `GEMINI_API_KEY` in `buffet_backend/secrets.py`) so Gemini can generate.
- The first RAG request will create/update a `chroma_db/` folder at the repo root for the persistent embedding store.
- Ticker detection is limited to a small curated list; when present, a lightweight market snapshot from `yfinance` is added as background context.

## Project Structure

```text
buffet-backend/
├── financials_api/
│   ├── data/
│   │   └── qa_corpus.csv  <-- Place your corpus here
│   ├── migrations/
│   ├── views/
│   │   ├── init.py
│   │   ├── chatbotviews.py  (Gemini View)
│   │   ├── finviews.py      (Financials View)
│   │   └── rag_view.py        (RAG View)
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── generator.py       <-- Legacy T5 generator (unused by current RAG)
│   ├── rag_generator.py   <-- Gemini Generator (RAG)
│   ├── rag_retriever.py   <-- Chroma + embeddings retriever
│   ├── rag_data.py        <-- Excel loader for Soros Q&A
│   ├── interface.py       <-- RAG Interface Logic (Gemini + Chroma)
│   ├── models.py
│   ├── retriever.py       <-- RAG Retriever Logic
│   ├── tests.py
│   └── urls.py            <-- App URLs (financials, chatbot, ragbot)
├── buffet_backend/        <-- Project settings directory
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py        <-- Project settings (CORS here)
│   ├── urls.py            <-- Project URLs (includes api/)
│   └── wsgi.py
├── manage.py              <-- Django management script
├── requirements.txt       <-- Python dependencies
├── secrets.py             <-- Gemini API Key (MUST be in .gitignore)
└── .gitignore             <-- Git ignore file

```
