import json

# 1. Corpus file load karna
try:
    with open("corpus.json", "r", encoding="utf-8") as f:
        corpus = json.load(f)
        text = corpus.get("doc1", "")
except Exception:
    text = "Artificial intelligence and machine learning are transforming modern technology rapidly. NLP helps computers understand human language easily."

print("Original Text:", text)

# 2. Fixed-size Chunking (Character-based)
def create_chunks(text, chunk_size=30, overlap=5):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

chunks = create_chunks(text, chunk_size=30, overlap=5)

print("\n--- Task 2: Text Chunks ---")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: '{chunk}'")