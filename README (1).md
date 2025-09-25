

# 🎓 AI-Powered Personalized Tutoring System

This project is a smart, adaptive learning assistant designed to enhance the student learning experience. Powered by advanced AI, it provides **real-time feedback**, **dynamic assessments**, **personalized learning paths**, and a user-friendly interface for both students and educators.

---

## ✨ Features

- 📊 **AI-Driven Assessments** – Dynamically generate quizzes and evaluate user responses using LLMs.
- 🧠 **Adaptive Learning Paths** – Progress adjusts based on user performance and comprehension level.
- 💬 **Chatbot Assistance** – Real-time AI chatbot to clear doubts instantly.
- 📚 **Personalized Course Recommendations** – Suggests topics based on individual progress and interest.
- 📈 **Performance Tracking Dashboard** – Visual insights on student strengths and areas for improvement.
- 🔁 **Module Skipping & Revision** – Users can skip or revisit modules depending on performance.
- ⚡ **Lightweight & Efficient** – Runs smoothly on edge devices; no heavy backend infrastructure required.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-tutoring-system.git
cd ai-tutoring-system
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed.
```bash
pip install -r requirements.txt
```

### 3️⃣ Prepare the Model
The project uses a locally optimized LLM for inference.

```bash
# Run once to setup model
python app.py
```

---

## 🖥️ Running the Application

### ▶️ Start Backend (FastAPI)
```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

### ▶️ Start Frontend (Streamlit)
In a new terminal:
```bash
streamlit run frontend.py
```

Now, go to [http://localhost:8501](http://localhost:8501) in your browser to use the app.

---

## 🔌 API Endpoints

| Method | Endpoint     | Description                                 |
|--------|--------------|---------------------------------------------|
| POST   | `/analyze`   | Analyzes quiz answers and gives feedback    |
| POST   | `/recommend` | Recommends personalized modules             |
| POST   | `/chatbot`   | Interact with the AI tutor for queries      |

### 📦 Example API Call
```python
import requests

response = requests.post("http://localhost:8000/analyze", json={"answers": [1, 2, 3]})
print(response.json())
```

---

## 🖼️ Screenshots

### 🧪 Assessment Panel
![Assessment](screenshots/assessment.png)

### 📈 Performance Tracker
![Tracker](screenshots/performance.png)

### 💬 Chatbot Interaction
![Chatbot](screenshots/chatbot.png)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, raise issues, or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For queries or suggestions, reach out at: **your-email@example.com**

