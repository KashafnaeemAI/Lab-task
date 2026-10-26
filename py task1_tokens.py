import json
import re

# 1. Corpus file load karna
with open("corpus.json", "r") as f:
    corpus = json.load(f)

# Pehle document ka text lena
text = corpus["doc1"]
print("Original Text:", text)

# 2. Method 1: Simple split (Whitespace Tokenization)
tokens_space = text.split()
print("\n--- Method 1: Whitespace Tokenization ---")
print("Tokens:", tokens_space)
print("Total Tokens:", len(tokens_space))

# 3. Method 2: Regex Tokenization (Words only)
tokens_regex = re.findall(r"\w+", text)
print("\n--- Method 2: Regex Tokenization ---")
print("Tokens:", tokens_regex)
print("Total Tokens:", len(tokens_regex))