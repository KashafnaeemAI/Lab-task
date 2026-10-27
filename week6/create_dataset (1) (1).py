import json

docs = {
    "doc1": "Late submission is normally penalized. Students with illness may request an extension with medical evidence before the deadline. Make sure to attach proper documents from doctor.",
    "doc2": "Submit the assignment as a PDF through the learning portal LMS. Assignments submitted via email will not be accepted.",
    "doc3": "Reset a forgotten password using the recovery link. Never share recovery codes or passwords with anyone else.",
    "doc4": "Contractors may work remotely only when the signed contract explicitly permits remote work. Employee rules do not apply directly.",
    "doc5": "For blank printer pages check ink levels and run the cleaning utility. Print a test page afterwards."
}

queries = [
    {"query": "What is required for illness extensions?", "doc": "doc1", "evidence": "medical evidence", "split": "dev"},
    {"query": "How do I reset a forgotten password?", "doc": "doc3", "evidence": "recovery link", "split": "dev"},
    {"query": "Where do I upload assignments?", "doc": "doc2", "evidence": "learning portal", "split": "dev"},
    {"query": "Can contractors work remotely?", "doc": "doc4", "evidence": "signed contract", "split": "dev"},
    {"query": "What do I do for blank printer pages?", "doc": "doc5", "evidence": "ink levels", "split": "test"},
    {"query": "How can I recover my login access?", "doc": "doc3", "evidence": "recovery link", "split": "test"},
    {"query": "How should I hand in my coursework?", "doc": "doc2", "evidence": "learning portal", "split": "test"},
    {"query": "What proof is needed when I was ill?", "doc": "doc1", "evidence": "medical evidence", "split": "test"},
    {"query": "What are tomorrow flight prices?", "doc": None, "evidence": None, "split": "test"},
    {"query": "Who won the football match?", "doc": None, "evidence": None, "split": "test"}
]

with open("corpus.json", "w") as f:
    json.dump(docs, f, indent=2)

with open("queries.json", "w") as f:
    json.dump(queries, f, indent=2)

print("corpus.json and queries.json created successfully!")