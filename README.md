
## 🏥 Medical Voice Assistant

An AI-powered real-time medical voice assistant built using Python, Streamlit, Whisper, LangGraph, and Groq LLM.

This project allows users to communicate with an AI assistant using voice input. The system converts speech to text, processes the request using an LLM-powered LangGraph workflow, and responds with both text and AI-generated voice output.

---

# ✨ Features

- 🎤 Real-time Voice Input
- 🧠 Session-based AI Memory
- 🤖 AI Medical Assistant
- 🔊 AI Voice Response
- ⚡ LangGraph Workflow Routing
- 🚨 Emergency Intent Detection
- 💬 Conversation History
- 🖥 Smart Streamlit UI
- 🧩 Modular Backend Architecture
- 🔒 Environment Variable Security

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Backend |
| Streamlit | Frontend UI |
| Whisper | Speech-to-Text |
| Groq LLM | AI Response Generation |
| LangGraph | AI Workflow Orchestration |
| LangChain | LLM Integration |
| pyttsx3 | Text-to-Speech |
| FFmpeg | Audio Processing |

---

# 🏗 Project Architecture

```text
medical-voice-chatbot/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── services/
│   │   ├── speech_service.py
│   │   ├── tts_service.py
│   │   └── llm_service.py
│   │
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── builder.py
│
├── ui/
│   └── streamlit_app.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ System Workflow

```text
User Voice
    ↓
Speech-to-Text (Whisper)
    ↓
LangGraph Intent Routing
    ↓
Groq LLM Processing
    ↓
AI Response Generation
    ↓
Text-to-Speech
    ↓
AI Voice Reply
```

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/maksudrakib44/Medical-Voice-Assistant.git

cd Medical-Voice-Assistant
```

---

# 2️⃣ Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Install FFmpeg

Download FFmpeg:

https://www.gyan.dev/ffmpeg/builds/

Recommended:

```text
ffmpeg-release-essentials.zip
```

Extract and add the `bin` folder to Windows Environment Variables PATH.

Verify installation:

```bash
ffmpeg -version
```

---

# 5️⃣ Setup Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama3-8b-8192
```

Get Groq API Key:

https://console.groq.com/keys

---

# ▶️ Run The Project

```bash
streamlit run ui/streamlit_app.py
```

---

# 🖥 UI Features

- 🎤 One-click voice recording
- 🔊 AI voice playback
- ⏹ Stop AI voice anytime
- 🧠 Session memory
- 💬 Conversation history
- 📌 User instructions sidebar
- 🩺 Medical assistant interface

---

# 🧠 LangGraph Concepts Used

## Nodes

- Intent Detection Node
- Emergency Response Node
- Medical AI Node

## State

Shared conversation state across workflow:

```python
{
    "text": "",
    "intent": "",
    "response": "",
    "history": []
}
```

## Conditional Routing

```text
Emergency Intent?
    ├── YES → Emergency Handler
    └── NO → Medical AI
```

---

# 🚨 Medical Disclaimer

This project is intended for educational and research purposes only.

It does NOT replace:
- licensed doctors
- medical diagnosis
- emergency services

Always seek professional medical help for serious conditions.

---

# 🔮 Future Improvements

- 📄 Medical PDF RAG
- 🧠 Persistent Long-Term Memory
- 🌐 FastAPI Backend
- 📱 Mobile-Friendly UI
- 🗣 Multilingual Support
- 🔄 Real-time Streaming Voice
- ☁ Cloud Deployment
- 👨‍⚕ Doctor Recommendation System

---

#  Live Preview:

    Visit: https://medivoiceai.streamlit.app/

## Home Screen

- Voice Recording
- AI Medical Conversation
- Session Memory
- Voice Controls

---

# 🧪 Example Conversation

```text
User:
I have fever and headache.

AI:
How long have you been experiencing these symptoms?

User:
Since yesterday.

AI:
Persistent fever and headache may indicate viral infection...
```

---

# 🛠 Requirements

- Python 3.11 Recommended
- FFmpeg Installed
- Internet Connection
- Groq API Key

---

# 📌 Important Notes

- Python 3.13 may cause dependency issues
- Python 3.11 is recommended
- `.env` should never be pushed to GitHub
- Whisper model downloads automatically on first run

---

# 👨‍💻 Author

## Md. Maksudul Haque

Computer Science & Engineering Graduate  
AI Enthusiast | AI Engineer | Research Learner

GitHub:

https://github.com/maksudrakib44

---

# ❤️ Acknowledgements

- OpenAI Whisper
- LangChain
- LangGraph
- Groq
- Streamlit

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🧠 Learn and improve it
- 🚀 Build your own AI systems

---