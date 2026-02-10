# Reflex AI

**AI-Powered Stock & Macro Risk Analysis Platform**

Reflex AI is a full-stack financial intelligence platform that combines **fundamental analysis, macro-risk diagnostics, and AI-driven market reasoning** into a single, explainable system.

Inspired by George Soros’s concept of *reflexivity*, the platform goes beyond static ratios and price charts to analyze **how fundamentals, leverage, liquidity, narratives, and market context interact** — and how those interactions amplify risk.

> ⚠️ Educational and research purposes only. Not financial advice.

---

## 🌍 Why Reflex AI?

Most financial tools answer **“what happened?”**
Reflex AI is built to explore **“why risk is building — and how it might evolve.”**

Markets are not purely efficient systems:

* perceptions influence prices
* prices influence fundamentals
* narratives influence behavior
* behavior feeds back into reality

Reflex AI is designed to **model and explain those feedback loops**, not just display numbers.

---

## 🧠 Core Capabilities

### 1️⃣ Stock Financial Analysis (Fundamentals Layer)

Reflex AI fetches **annual financial statements** for publicly traded companies and presents them in a clean, structured dashboard:

* Income Statement
* Balance Sheet
* Cash Flow Statement

Data is sourced via `yfinance` and normalized for downstream analysis.

---

### 2️⃣ Soros-Style Risk Diagnostics (Risk Layer)

Instead of generic ratios, Reflex AI computes **risk-focused diagnostics** aligned with macro and reflexive thinking:

**Liquidity Risk**

* Ability to survive stress without external financing
* Cash adequacy relative to obligations

**Leverage Risk**

* Debt burden vs equity and earnings power
* Sensitivity to tightening financial conditions

**Profitability Resilience**

* Consistency of operating performance
* Quality of earnings vs cash generation

Each risk check is:

* explainable
* contextual
* designed to highlight *fragility*, not just performance

---

### 3️⃣ AI Market Reasoning (Intelligence Layer)

Reflex AI provides two AI interaction modes:

#### 🔹 Gemini Mode

* Direct interaction with Google’s Gemini LLM
* Prompted to reason in the **philosophical style of George Soros**
* Focuses on:

  * reflexivity
  * market psychology
  * systemic risk
  * second-order effects

Use case:

> “What would Soros worry about in a high-leverage tech company during rising rates?”

---

#### 🔹 RAG Mode (Retrieval-Augmented Generation)

A **grounded, explainable AI system** built using:

* **ChromaDB** for vector storage
* **Sentence-Transformer embeddings** for semantic retrieval
* **Curated Soros-focused Q&A corpus**
* **Gemini** for final response generation

How it works:

1. User query is semantically matched against a Soros knowledge base
2. Relevant concepts are retrieved
3. Optional **ticker-aware market snapshot** is injected
4. Gemini generates a response grounded in retrieved context

This avoids hallucination and ensures **conceptual consistency**.

---

### 4️⃣ Ticker-Aware Market Context

When a recognizable stock ticker is detected:

* Reflex AI fetches a lightweight market snapshot
* This contextual data informs the AI’s reasoning
* Responses feel *situated*, not abstract

Example:

> “How would reflexivity apply to TSLA right now?”

---

### 5️⃣ Pairs Trading Analysis (Experimental)

The frontend includes an exploratory **pairs-trading interface** for studying mean-reversion behavior:

* Hedge ratio estimation
* Cointegration testing (when available)
* Z-score snapshot
* Trade simulation & cumulative P&L

This feature is intended as a **research sandbox**, not a production trading system.

---

<img width="1334" height="825" alt="image" src="https://github.com/user-attachments/assets/4d3393fa-92be-4ca5-8a22-d1ab6d340196" />

---

## Data Foundations (What enters the system)

Reflex AI operates on **three distinct data classes**, each serving a different cognitive role.

---

### Market & Financial Statement Data (Quantitative Reality Layer)

**Source**

* `yfinance` (Yahoo Finance API wrapper)

**Data Retrieved**

* Annual Income Statement
* Annual Balance Sheet
* Annual Cash Flow Statement
* Lightweight market snapshot (price, recent behavior, metadata)

**Why this data matters**
Financial statements represent the **current accounting reality** of a company:

* capital structure
* operating performance
* cash generation
* balance-sheet resilience

This is the *baseline truth* against which risk is assessed.

**Important design choice**

* Annual data is used intentionally
  → avoids short-term noise
  → aligns with macro & structural analysis rather than trading signals

---

### Soros Knowledge Corpus (Narrative & Conceptual Layer)

**Source**

* Curated Q&A corpus (`qa_corpus.csv` or `Soros_Questions.xlsx`)

**Content**

* Concepts related to:

  * reflexivity
  * market psychology
  * leverage cycles
  * bubbles & crashes
  * uncertainty and fallibility
  * macro regime shifts

**Why this data exists**
Markets are not driven purely by numbers.
They are driven by:

* beliefs
* narratives
* expectations
* collective behavior

This corpus acts as a **conceptual memory** that allows the AI to reason *in context*, rather than hallucinating explanations.

---

### User Queries (Intent Layer)

**Source**

* Natural language questions from the UI

**Examples**

* “What risks does NVDA face in a high-rate environment?”
* “How would Soros think about leverage in tech stocks?”
* “Is liquidity a hidden risk for this company?”

These queries define:

* *what lens to apply*
* *which concepts to retrieve*
* *how deep the reasoning should go*

---

## 2. Data Processing & Transformation

Once raw data enters the system, it is **normalized, structured, and transformed** into intermediate representations.

---

### Financial Normalization

**Steps**

* Raw financial tables → Pandas DataFrames
* Missing or inconsistent fields handled gracefully
* Statements aligned by fiscal year
* Converted into JSON-serializable structures

**Outcome**
A clean, structured financial dataset suitable for:

* ratio computation
* risk diagnostics
* UI rendering
* AI context injection

---

### Soros-Style Risk Diagnostics (Quant → Insight)

Instead of generic financial ratios, Reflex AI computes **risk-centric diagnostics** designed to surface *fragility*.

#### Liquidity Risk

Assesses:

* ability to meet obligations without external funding
* dependence on continuous capital access

This highlights **liquidity illusion** — where firms appear stable until funding dries up.

---

#### Leverage Risk

Assesses:

* debt burden relative to equity and earnings power
* exposure to tightening financial conditions

Leverage is treated as a **non-linear risk amplifier**, not just a balance-sheet statistic.

---

#### Profitability Resilience

Assesses:

* consistency of operating income
* quality of earnings vs cash flow
* margin stability across time

This separates **accounting profitability** from **economic durability**.

---

**Why this matters**
In reflexive systems:

* leverage magnifies perception
* perception magnifies price
* price feeds back into fundamentals

These diagnostics are explicitly designed to expose that loop.

---

## Intelligence Layer (Reasoning Architecture)

This is where Reflex AI moves from **calculation → cognition**.

---

### Gemini Reasoning Mode (Ungrounded Intelligence)

**Flow**
User Query
→ Prompted Gemini LLM
→ Response styled around Soros-like reasoning

**Characteristics**

* High-level philosophical reasoning
* Narrative explanations
* Macro framing

**Strength**

* Flexible
* Conceptual
* Exploratory

**Limitation**

* Relies entirely on the model’s internal knowledge
* No grounding in a controlled corpus

---

### RAG Reasoning Mode (Grounded Intelligence)

This is the **core technical innovation** of the system.

---

#### Step 1: Semantic Encoding

* User query embedded using a sentence-transformer
* Embeddings capture *meaning*, not keywords

---

#### Step 2: Vector Retrieval (ChromaDB)

* Query embedding compared against Soros corpus embeddings
* Most semantically relevant concepts retrieved

This ensures:

* conceptual alignment
* reduced hallucination
* consistent philosophical grounding

---

#### Step 3: Context Assembly

The system assembles:

* retrieved Soros concepts
* optional ticker-specific market snapshot
* concise financial context

This forms a **bounded reasoning window**.

---

#### Step 4: Gemini Generation

Gemini generates the final response using:

* retrieved knowledge
* current market context
* user intent

The model is no longer “free-thinking” — it is **anchored**.

---

### Why RAG is critical here

Reflexivity is subtle and easy to misrepresent.

RAG ensures:

* the AI stays philosophically consistent
* responses reflect *ideas Soros actually expressed*
* explanations are traceable to a knowledge base

---

## Ticker-Aware Market Context Injection

When a known ticker is detected:

* the system fetches a minimal market snapshot
* avoids overwhelming the LLM with raw price series
* provides situational awareness

This enables answers like:

> “Given recent market enthusiasm, leverage here becomes reflexively dangerous…”

without turning the system into a trading bot.

---

## Frontend → Backend → Intelligence → Output

### End-to-End Flow

1. User enters ticker or question
2. Frontend calls backend API
3. Backend:

   * fetches financials
   * computes risk diagnostics
   * optionally performs RAG retrieval
4. Gemini synthesizes reasoning
5. Response returned to UI
6. User sees:

   * structured data
   * interpretable risk signals
   * narrative explanation

---

## Final Outputs (What the user gets)

### Quantitative Outputs

* Financial statements
* Risk diagnostics
* Pairs trading analytics (experimental)

### Qualitative Outputs

* Narrative explanations
* Macro-style reasoning
* Conceptual framing of risk

### Cognitive Output

* Understanding *why* a situation may be fragile
* Awareness of second-order effects
* Insight into how perception and fundamentals interact

---

## Why This System Is Different

Reflex AI is **not**:

* a price predictor
* a signal generator
* a trading bot

It **is**:

* a reasoning system
* a risk interpretation engine
* a reflexive market analysis lab

---

## 📡 API Endpoints

### Financials

```
GET /api/financials/<ticker>/
```

Returns:

* Annual financial statements
* Soros-style risk diagnostics

---

### Gemini Chatbot

```
POST /api/chatbot/
```

Request:

```json
{ "message": "Your question" }
```

---

### RAG Chatbot

```
POST /api/ragbot/
```

Request:

```json
{ "message": "Your question" }
```

---

## 🧪 Design Philosophy

Reflex AI is built around five principles:

1. **Risk over returns**
   Fragility matters more than upside.

2. **Explainability over prediction**
   Understanding systems beats forecasting noise.

3. **Narratives matter**
   Markets move on beliefs, not just balance sheets.

4. **Feedback loops dominate**
   Prices change fundamentals, not just reflect them.

5. **AI as a reasoning partner, not an oracle**
   Grounded insight > confident hallucination.

---

## 🚧 Known Limitations

* Market data is end-of-day (via yfinance)
* Ticker detection is intentionally conservative
* Vector index persistence depends on filesystem configuration
* No execution, order routing, or live trading support

---

## 8. Intended Audience

* AI & ML engineers
* Data engineers
* Product managers
* Financial systems researchers
* Anyone studying complex adaptive systems

---

## 🔮 Future Directions

* Agent-based macro simulations
* Scenario stress testing (rates, liquidity shocks)
* Cross-asset reflexivity analysis
* Narrative drift detection
* Portfolio-level systemic risk views

---

## 🛡️ Disclaimer

This project is **for educational and research purposes only**.
It does not constitute financial advice, investment recommendations, or trading signals.

