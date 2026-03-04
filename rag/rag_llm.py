import subprocess
from vector_search import search

MODEL = "mistral"

def ask_llm(prompt):
    result = subprocess.run(
        ['ollama','run',MODEL],
        input=prompt,
        text=True,
        capture_output=True,
        encoding='utf-8',
        errors='ignore'
    )
    return result.stdout

def ask_physics(question):
    result, top_score = search(question)

    if top_score < 0.4:
       return "I don't know this topic yet."
    context = "\n\n".join([r['text'] for r in result])
    prompt = f"""
      You are a physics teacher.

      Answer ONLY using the context below.

      If the answer is not in the context, say:
      "I don't know this topic yet."

     Context:
       {context}

    Question:
       {question}
"""

    ans = ask_llm(prompt)
    return ans