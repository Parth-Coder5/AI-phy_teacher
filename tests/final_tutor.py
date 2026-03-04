from rag_llm import ask_physics

while True:

    q = input("\nAsk Physics Question: ")

    if q.lower() == "exit":
        break

    answer = ask_physics(q)

    print("\nAI Teacher:\n")
    print(answer)