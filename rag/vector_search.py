import json 
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print('Loading Embedding Model...')
model = SentenceTransformer('all-MiniLM-L6-v2')

with open('knowledge_base.json', 'r', encoding='utf-8') as f:
    kb = json.load(f)

text = [chunk['text']for chunk in kb]

print('Create Embeddings...')
embedding = model.encode(text)

def search(query,top_k=3):
    query_vec = model.encode([query])

    scores = cosine_similarity(query_vec, embedding)[0]

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    top_score = scores[top_indices[0]]

    for i in top_indices:
       results.append(kb[i])

    return results, top_score