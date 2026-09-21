import streamlit as st
from huggingface_hub import InferenceClient

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Sejal AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Hugging Face Authentication
# -----------------------------

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    api_key=HF_TOKEN
)

MODEL = "openai/gpt-oss-120b:fastest"

# -----------------------------
# System Instructions
# -----------------------------

DEFAULT_INSTRUCTION = """
You are a helpful AI study assistant for a B.Tech AIML student.
Explain technical concepts clearly using simple language and examples.
Be accurate, concise and encouraging.
"""

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": DEFAULT_INSTRUCTION
        }
    ]

# -----------------------------
# Header
# -----------------------------

st.title("🤖 Sejal AI Study Assistant")

st.write(
    "Ask questions, learn concepts and have a context-aware conversation with AI."
)

st.divider()

# -----------------------------
# Custom Instructions
# -----------------------------

with st.expander("⚙️ Custom AI Instructions"):

    custom_instruction = st.text_area(
        "How should the AI behave?",
        value=DEFAULT_INSTRUCTION,
        height=120
    )

# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------

user_prompt = st.chat_input("Ask me anything...")

if user_prompt:

    st.session_state.messages[0]["content"] = custom_instruction

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    try:

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = client.chat.completions.create(
                    model=MODEL,
                    messages=st.session_state.messages,
                    max_tokens=300
                )

                assistant_reply = response.choices[0].message.content

                if not assistant_reply:
                    assistant_reply = "Sorry, I could not generate a response."

                st.markdown(assistant_reply)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

    except Exception as error:

        st.error(
            f"Sorry, something went wrong: {type(error).__name__}"
        )

# -----------------------------
# Clear Chat
# -----------------------------

st.divider()

if st.button("🧹 Clear Conversation"):

    st.session_state.messages = [
        {
            "role": "system",
            "content": DEFAULT_INSTRUCTION
        }
    ]

    st.rerun()
