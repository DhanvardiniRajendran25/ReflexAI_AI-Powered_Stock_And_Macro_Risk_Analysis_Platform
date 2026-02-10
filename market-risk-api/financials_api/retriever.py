
import os
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None

class SimpleQARetriever:
    def __init__(self, corpus_path: str):
        self.corpus_path = corpus_path
        self.questions = []
        self.answers = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.question_vectors = None
        self.semantic_model = None
        self.question_embeddings = None

        # print(f"Loading Q&A corpus from: {self.corpus_path}") # Minimal Comments
        try:
            with open(self.corpus_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, quotechar='"', delimiter=',', skipinitialspace=True)
                for i, row in enumerate(reader):
                    if len(row) == 2:
                        question, answer = row
                        self.questions.append(question.strip())
                        self.answers.append(answer.strip())

            if not self.questions:
                 print("Warning: No questions loaded from corpus.")
            else:
                 # print(f"Loaded {len(self.questions)} Q&A pairs.") # Minimal Comments
                 self.question_vectors = self.vectorizer.fit_transform(self.questions)
                 # print("TF-IDF Vectorizer fitted on questions.") # Minimal Comments
                 if SentenceTransformer is not None:
                     try:
                         self.semantic_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
                         self.question_embeddings = self.semantic_model.encode(self.questions, convert_to_numpy=True, normalize_embeddings=True)
                     except Exception as e:
                         print(f"Warning: Failed to load sentence-transformer model: {e}")
                         self.semantic_model = None

        except FileNotFoundError:
            print(f"Error: Corpus file not found at {self.corpus_path}")
            raise

    def retrieve_top_k(self, query: str, k: int = 3):
        results = []
        if not self.questions:
            return results

        try:
            if self.semantic_model is not None and self.question_embeddings is not None:
                q_emb = self.semantic_model.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]
                sims = np.dot(self.question_embeddings, q_emb)
            else:
                if self.question_vectors is None:
                    return results
                query_vec = self.vectorizer.transform([query])
                sims = (query_vec * self.question_vectors.T).toarray()[0]

            num_docs = len(self.questions)
            actual_k = min(k, num_docs)
            if actual_k > 0:
                top_indices = np.argsort(sims)[::-1][:actual_k]
                for idx in top_indices:
                    results.append({
                        "doc_name": os.path.basename(self.corpus_path),
                        "similarity": float(sims[idx]),
                        "text": self.answers[idx], # Answer text for context
                        "matched_question": self.questions[idx]
                    })
        except Exception as e:
            print(f"Error during retrieval: {e}")
            return []

        return results
