# 🧠 AI Physics Teacher

A **Retrieval-Augmented Generation (RAG)** based AI system that answers physics questions using a **custom-built knowledge base**.

This project combines **embeddings, vector search, and a local LLM (Mistral via Ollama)** to simulate a **syllabus-aware AI physics teacher**.

The system retrieves relevant physics concepts from its internal knowledge base and uses an LLM to generate clear explanations.

---

# 🚀 Features

✅ Retrieval-Augmented Generation (RAG) architecture
✅ Custom physics knowledge base
✅ Vector similarity search using embeddings
✅ Local LLM inference with **Ollama + Mistral**
✅ Context-aware explanations
✅ Prevents hallucinations using similarity thresholds
✅ Modular architecture for adding more physics chapters

---

# 📚 Current Knowledge Scope

⚠️ **Important**

The current version of the AI teacher only supports questions from:

**Class 11 Physics — Motion in 1D**

Supported topics include:

• Distance vs Displacement
• Speed vs Velocity
• Acceleration
• Equations of Motion
• Motion Graphs (x-t, v-t, a-t)

If a question outside this syllabus is asked, the system will respond:

> *"I don't know this topic yet."*

This ensures answers are restricted to the project's knowledge base.

---

# 🧠 System Architecture

User Question
↓
Embedding Generation
↓
Vector Similarity Search
↓
Relevant Knowledge Retrieval
↓
Context Injection
↓
Local LLM (Mistral via Ollama)
↓
Generated Physics Explanation

This architecture follows the **RAG (Retrieval-Augmented Generation)** pattern used in many modern AI systems.

---

# 📁 Project Structure

```
AI-phy_teacher
│
├── class11/
│   └── motion_1d/
│       ├── acc.py
│       ├── distance_displacement.py
│       ├── speed_velocity.py
│       ├── equations_motion.py
│       └── graphs_motion.py
│
├── data/
│   └── knowledge_base.json
│
├── rag/
│   ├── rag_llm.py
│   └── vector_search.py
│
├── builds/
│   └── build_knowledge_base.py
│
├── tests/
│   ├── brain_test.py
│   └── final_tutor.py
│
├── README.md
├── requirements.txt
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Parth-Coder5/AI-phy_teacher.git
cd AI-phy_teacher
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install **Ollama**:

https://ollama.com

Pull the Mistral model:

```bash
ollama pull mistral
```

---

# ▶️ Running the AI Teacher

Run the chatbot:

```bash
python final_test.py
```

Then ask a physics question:

```
Ask Physics Question: What is acceleration?
```

Example output:

```
AI Teacher:

Acceleration is the rate of change of velocity with respect to time...
```

---

# 🧩 How It Works

1️⃣ Physics concepts are stored in a **structured knowledge base**
2️⃣ The system converts questions into **embeddings**
3️⃣ A **vector search** retrieves the most relevant concepts
4️⃣ Retrieved context is injected into the prompt
5️⃣ The **local LLM generates a natural explanation**

This allows the system to answer questions using **only its internal knowledge**.

---

# 🔧 Technologies Used

• Python
• Sentence Transformers
• NumPy
• Scikit-learn
• Ollama
• Mistral LLM

---

# 📌 Future Improvements

Planned upgrades for the project:

• Add more Class 11 chapters
• Support Class 12 Physics
• Streamlit Web Interface
• Step-by-step numerical solving
• Graph visualization
• Voice interaction

---

# 👨‍💻 Author

**Kavyansh Mishra**

Student developer interested in:

• Artificial Intelligence
• Machine Learning
• Physics simulations
• Building real-world AI tools

GitHub:
https://github.com/Parth-Coder5

---

# ⭐ If you like this project

Consider giving the repository a **star ⭐**
