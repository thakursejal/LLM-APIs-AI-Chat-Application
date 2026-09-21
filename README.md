# 🤖 LLM APIs & AI Chat Application

**Module 3 — Codomax Digital Solutions Internship**

**Name:** Thakur Sejal

## 📌 Overview

This repository contains my work for **Module 3: LLM APIs & Application Development**.

The project demonstrates how to connect a Python application to a Large Language Model through an API and build a conversational AI application with chat history, custom instructions, error handling and a web-based interface.

---

# 🎯 Module Objectives

The main objectives of this module are:

- Understand LLM APIs.
- Learn API authentication.
- Use environment variables and secrets securely.
- Connect an LLM to a Python application.
- Manage conversation history.
- Understand system, user and assistant messages.
- Work with model parameters.
- Monitor token usage.
- Generate structured responses.
- Implement API error handling.
- Understand basic API usage management.
- Build an AI chat application.
- Deploy the application using Streamlit.

---

# 📚 Module Contents

## 1️⃣ LLM APIs & Authentication

Topics covered:

- Introduction to LLM APIs
- API requests and responses
- API authentication
- API keys and access tokens
- Environment variables
- Secure credential management
- Model selection
- Model parameters

### Practical Work

A Python application was connected to a Hugging Face LLM through an API.

The API workflow was demonstrated as:

**Python → Authentication → Hugging Face API → Inference Provider → LLM → AI Response**

---

## 2️⃣ Conversation Management

Topics covered:

- System messages
- User messages
- Assistant messages
- Chat history
- Multi-turn conversations
- Context management
- Model parameters
- Token usage
- Context windows

### Practical Work

A multi-turn conversation was implemented using Python.

The application stored previous messages and sent the conversation history with new requests to maintain context.

---

## 3️⃣ Structured Responses & Error Handling

Topics covered:

- Structured AI responses
- JSON output
- API error handling
- Exception handling
- Token usage
- Output limits
- Basic API usage management
- Secure API credential handling

### Practical Work

The project demonstrated:

- Structured JSON responses
- Error handling using `try-except`
- Token usage monitoring
- Maximum output token control

---

## 4️⃣ AI Chat Application

The main project of this module is an AI-powered study assistant.

### Features

- 🤖 AI chat interface
- 💬 Multi-turn conversations
- 🧠 Conversation history
- ⚙️ Custom AI instructions
- 🔐 Secure API token handling
- 🛡️ Error handling
- 🧹 Clear conversation feature
- 🌐 Streamlit web interface

---

# 🛠️ Technologies Used

- Python
- Google Colab
- Hugging Face Inference API
- Hugging Face Hub
- Streamlit
- GitHub
- Large Language Models
- API Authentication
- JSON

---

# 🔄 Application Workflow

The application follows this workflow:

**User Input → Chat History → LLM API → AI Response → Updated Chat History → Display**

For deployment:

**Python Application → GitHub → Streamlit Community Cloud → Live Web Application**

---

# 🧠 AI Study Assistant

The application is designed as a study assistant for B.Tech students.

The default AI instruction is:

"You are a helpful AI study assistant for a B.Tech AIML student. Explain technical concepts clearly using simple language and examples."

Users can also provide custom instructions to change the AI's response behavior.

---

# 💬 Conversation Management

The chatbot maintains messages using three main roles:

- `system`
- `user`
- `assistant`

This allows the application to maintain context across multiple questions.

Example workflow:

**User Question → AI Response → Store History → Follow-up Question → Context-Aware Response**

---

# 🛡️ Error Handling

The application uses exception handling to prevent API failures from crashing the application.

Possible API problems include:

- Invalid requests
- Authentication problems
- Unsupported models
- Provider errors
- Network problems
- Rate limits

Instead of exposing a technical traceback to the user, the application displays a simpler error message.

---

# 📊 Token Management

The project also demonstrates token usage monitoring.

Important concepts include:

- Input tokens
- Output tokens
- Total tokens
- Maximum output tokens
- Conversation history

Controlling output length and unnecessary conversation history can help manage API usage.

---

# 🔐 Security

API credentials should never be hard-coded into public source code.

The Streamlit application uses:

`st.secrets["HF_TOKEN"]`

The Hugging Face token should be stored in Streamlit's secret management system rather than uploaded to GitHub.

Never share API tokens in:

- GitHub repositories
- README files
- Screenshots
- Public notebooks
- Social media posts

---

# 📁 Repository Structure

The repository contains:

- `app.py` — Streamlit AI chat application
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
- `LLM_APIs_AI_Chat_Application_Thakur_Sejal.ipynb` — Module 3 practical notebook

---

# 🧪 Testing

The application was tested for:

| Feature | Status |
|---|---|
| LLM API Connection | ✅ |
| Authentication | ✅ |
| AI Response | ✅ |
| Chat History | ✅ |
| Multi-Turn Conversation | ✅ |
| Custom Instructions | ✅ |
| Structured Response | ✅ |
| Error Handling | ✅ |
| Token Management | ✅ |
| Clear Conversation | ✅ |
| Streamlit UI | ✅ |

---

# 🎓 Key Learning Outcomes

After completing this module, I learned how to:

- Connect Python applications to LLM APIs.
- Authenticate API requests securely.
- Use environment variables and secrets.
- Manage system, user and assistant messages.
- Maintain conversation history.
- Build multi-turn AI conversations.
- Generate structured responses.
- Handle API errors.
- Monitor token usage.
- Control response length.
- Build an AI chatbot interface.
- Deploy an AI application using Streamlit.

---

# 🌐 Deployment

The application is designed for deployment using:

**Streamlit Community Cloud**

The Hugging Face API token should be configured as a Streamlit secret during deployment.

## 🌐 Live Application

Try the deployed AI Study Assistant:

👉 https://llm-apis-ai-chat-application.streamlit.app/
---

# 👩‍💻 Author

**Thakur Sejal**

B.Tech — Artificial Intelligence & Machine Learning

---

# 🏆 Internship

**Codomax Digital Solutions Internship**

**Module 3: LLM APIs & Application Development**

---

## ⭐ Module 3 Completed

This project demonstrates the integration of LLM APIs with Python and the development of a conversational AI application with secure authentication, chat history, error handling and a Streamlit interface.# LLM-APIs-AI-Chat-Application
