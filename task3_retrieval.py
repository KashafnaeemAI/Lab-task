
import json
import math
import os

# 1. Corpus aur Queries load karna
current_dir = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(current_dir, "corpus.json")
queries_path = os.path.join(current_dir, "queries.json")

corpus = {}
queries = {}

if os.path.exists(corpus_path):
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus = json.load(f)

if os.path.exists(queries_path):
    with open(queries_path, "r", encoding="utf-8") as f:
        queries = json.load(f)

# Backup data agar files na milein
if not corpus:
    corpus = {
        "doc1": "Artificial intelligence and machine learning are transforming modern technology rapidly.",
        "doc2": "Natural language processing allows computers to understand human language and text efficiently."
    }

if not queries:
    queries = {
        "q1": "machine learning technology",
        "q2": "natural language processing"
    }

print("Loaded Corpus Documents:", len(corpus))
print("Loaded Queries:", len(queries))

# Helper Functions
def tokenize(text):
    return text.lower().split()

def compute_tf(doc_tokens):
    tf = {}
    total = len(doc_tokens)
    for word in doc_tokens:
        tf[word] = tf.get(word, 0) + 1 / total
    return tf

def compute_idf(corpus_tokens):
    N = len(corpus_tokens)
    idf = {}
    all_words = set(w for doc in corpus_tokens.values() for w in doc)
    for word in all_words:
        count = sum(1 for doc in corpus_tokens.values() if word in doc)
        idf[word] = math.log((N + 1) / (count + 1)) + 1
    return idf

def compute_tfidf(tf, idf):
    return {w: tf.get(w, 0) * idf.get(w, 0) for w in idf}

def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1.get(w, 0) * vec2.get(w, 0) for w in vec1)
    mag1 = math.sqrt(sum(v**2 for v in vec1.values()))
    mag2 = math.sqrt(sum(v**2 for v in vec2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot_product / (mag1 * mag2)

# Tokenize corpus
corpus_tokens = {doc_id: tokenize(text) for doc_id, text in corpus.items()}
idf = compute_idf(corpus_tokens)

# Compute TF-IDF for documents
corpus_tfidf = {}
for doc_id, tokens in corpus_tokens.items():
    tf = compute_tf(tokens)
    corpus_tfidf[doc_id] = compute_tfidf(tf, idf)

print("\n--- Task 3: Query Retrieval Results ---")
for q_id, q_text in queries.items():
    q_tokens = tokenize(q_text)
    q_tf = compute_tf(q_tokens)
    q_tfidf = compute_tfidf(q_tf, idf)

    scores = {}
    for doc_id, doc_vec in corpus_tfidf.items():
        scores[doc_id] = cosine_similarity(q_tfidf, doc_vec)

    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nQuery ({q_id}): '{q_text}'")
    for doc_id, score in sorted_docs:
        print(f"  -> {doc_id}: Similarity Score = {score:.4f}")
