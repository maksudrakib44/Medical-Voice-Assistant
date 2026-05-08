import sys
import os
import tempfile
import time

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
from streamlit_mic_recorder import mic_recorder

from app.services.speech_service import SpeechService
from app.services.tts_service import TTSService
from app.graph.builder import build_graph

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Medical Voice AI",
    page_icon="🏥",
    layout="centered"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(
    """
    <style>

    .main {
        padding-top: 1.5rem;
    }

    .footer {
        text-align: center;
        padding-top: 30px;
        padding-bottom: 10px;
        color: gray;
        font-size: 14px;
    }

    .guide-box {
        background-color: #f7f9fc;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e6e6e6;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SERVICES
# =====================================================
speech_service = SpeechService()
tts_service = TTSService()
graph = build_graph()

# =====================================================
# SESSION STATE
# =====================================================
if "history" not in st.session_state:
    st.session_state.history = []

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if "status" not in st.session_state:
    st.session_state.status = "🟢 Ready"

if "processing" not in st.session_state:
    st.session_state.processing = False

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.title("🏥")

    st.markdown(
        """
        ### 📌 Quick Guide

        - Click **Start Recording**
        - Speak naturally
        - Wait for AI response
        - AI can remember session conversation
        - Use **Stop Voice** anytime

        ---
        """
    )

    st.info(
        "This assistant provides general medical guidance only."
    )

# =====================================================
# HEADER
# =====================================================
st.title("🏥 Medical Voice Assistant")

st.markdown(
    """
    <div class="guide-box">
    🎤 Talk naturally with the AI medical assistant using your microphone.<br>
    🧠 The assistant remembers your conversation during the current session.
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# STATUS BAR
# =====================================================
st.info(f"Status: {st.session_state.status}")

# =====================================================
# CONTROL PANEL
# =====================================================
col1, col2 = st.columns(2)

with col1:

    stop_voice = st.button(
        "⏹ Stop Voice",
        use_container_width=True
    )

with col2:

    clear_chat = st.button(
        "🗑 Clear Chat",
        use_container_width=True
    )

# =====================================================
# STOP VOICE
# =====================================================
if stop_voice:

    tts_service.stop()

    st.session_state.status = "🔇 Voice Stopped"

# =====================================================
# CLEAR CHAT
# =====================================================
if clear_chat:

    tts_service.stop()

    st.session_state.history = []

    st.session_state.chat_messages = []

    st.session_state.status = "🧹 Chat Cleared"

# =====================================================
# MIC RECORDER
# =====================================================
audio = mic_recorder(
    start_prompt="🎤 Tap to Speak",
    stop_prompt="⏹ Send Voice",
    key="medical_voice_ai"
)

# =====================================================
# AUDIO PROCESSING
# =====================================================
if audio and not st.session_state.processing:

    st.session_state.processing = True

    # stop previous voice if running
    tts_service.stop()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as tmp:

        tmp.write(audio["bytes"])

        audio_path = tmp.name

    try:

        # =====================================================
        # SPEECH TO TEXT
        # =====================================================
        st.session_state.status = "🎧 Listening..."

        user_text = speech_service.transcribe(audio_path)

        # =====================================================
        # SHOW USER MESSAGE
        # =====================================================
        with st.chat_message("user"):

            st.write(user_text)

        # =====================================================
        # AI THINKING
        # =====================================================
        st.session_state.status = "🤖 Thinking..."

        result = graph.invoke({
            "text": user_text,
            "history": st.session_state.chat_messages
        })

        ai_response = result["response"]

        # =====================================================
        # AI RESPONSE STREAM EFFECT
        # =====================================================
        with st.chat_message("assistant"):

            response_box = st.empty()

            streamed_text = ""

            for word in ai_response.split():

                streamed_text += word + " "

                response_box.markdown(streamed_text)

                time.sleep(0.02)

        # =====================================================
        # SAVE UI HISTORY
        # =====================================================
        st.session_state.history.append({
            "user": user_text,
            "assistant": ai_response
        })

        # =====================================================
        # SAVE AI MEMORY
        # =====================================================
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_text
        })

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": ai_response
        })

        # =====================================================
        # TEXT TO SPEECH
        # =====================================================
        st.session_state.status = "🔊 Speaking..."

        tts_service.speak(ai_response)

        st.session_state.status = "🟢 Ready"

    except Exception as e:

        st.error(f"Error: {str(e)}")

        st.session_state.status = "❌ Error"

    finally:

        st.session_state.processing = False

        try:
            os.remove(audio_path)
        except:
            pass

# =====================================================
# CONVERSATION HISTORY
# =====================================================
if st.session_state.history:

    st.markdown("---")

    st.subheader("🧠 Conversation History")

    for item in reversed(st.session_state.history[-10:]):

        with st.chat_message("user"):

            st.write(item["user"])

        with st.chat_message("assistant"):

            st.write(item["assistant"])

# =====================================================
# FOOTER
# =====================================================
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Maksud
    </div>
    """,
    unsafe_allow_html=True
)