import streamlit as st
import random
import base64

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Happy Birthday My Doctor, This chatbot is for you. 💙",
    page_icon="💙",
    layout="centered"
)

# --------------------------------------------------
# BACKGROUND IMAGE + MEDICAL THEME
# --------------------------------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Background with dark medical overlay */
        .stApp {{
            background:
                linear-gradient(
                    rgba(0, 45, 90, 0.55),
                    rgba(0, 45, 90, 0.55)
                ),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* Make all normal text visible */
        h1, h2, h3, h4, h5, h6, p, span, label {{
            color: #ffffff !important;
        }}

        /* Chat bubbles */
        .stChatMessage {{
            background-color: rgb(200, 162, 200);
            color: #1f2937;
            border-radius: 16px;
            padding: 14px;
            margin-bottom: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        }}

        /* ECG */
        .ecg {{
            width: 100%;
            height: 60px;
            margin-top: -10px;
        }}

        .ecg svg {{
            width: 100%;
            height: 60px;
        }}

        .ecg path {{
            stroke: #4fc3f7;
            stroke-width: 2.5;
            fill: none;
            stroke-dasharray: 1000;
            stroke-dashoffset: 1000;
            animation: ecg-move 3s linear infinite;
        }}

        @keyframes ecg-move {{
            to {{ stroke-dashoffset: 0; }}
        }}

        /* Floating stethoscope */
        .stethoscope {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            font-size: 42px;
            animation: float 3s ease-in-out infinite;
            opacity: 0.9;
        }}

        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-12px); }}
            100% {{ transform: translateY(0px); }}
        }}

        /* Title shadow */
        h1 {{
            text-shadow: 0 2px 10px rgba(0,0,0,0.6);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# ADD BACKGROUND IMAGE (IMAGE MUST BE IN SAME FOLDER)
# --------------------------------------------------
add_bg_from_local("background.jpeg")

# --------------------------------------------------
# CHATBOT CONTENT
# --------------------------------------------------
responses = {
    "good": [
        "You handled today like a pro! Your patients are lucky to have you.",
        "See? You're built for this. White coat is getting closer.",
        "Celebrate the small wins – you're becoming an amazing doctor."
    ],
    "okay": [
        "Not every day has to be extraordinary. Showing up is a big deal.",
        "Slow, steady days also build strong doctors.",
        "Your consistency is quietly changing your future."
    ],
    "tough": [
        "It's okay to feel exhausted. Even heroes need rest.",
        "You're allowed to be tired and still be an amazing future doctor.",
        "Hard days don't mean you're weak; they mean you're still trying."
    ]
}

prescriptions = [
    "💧 Hydrate well and stretch your neck for 5 minutes.",
    "📱 Put phone away for 15 minutes and breathe deeply.",
    "🎵 Listen to one song that reminds you of us.",
    "😴 Sleep a little earlier tonight. Your brain deserves it."
]

love_lines = [
    "No matter how your day was, I'm always proud of you.",
    "One day, your patients will thank you for not giving up.",
    "Remember: you're not alone. I'm with you always."
]

# --------------------------------------------------
# CHATBOT LOGIC
# --------------------------------------------------
def get_response(message):
    message_lower = message.lower()

    if any(word in message_lower for word in ["good", "great", "nice", "awesome", "best"]):
        mood = "good"
    elif any(word in message_lower for word in ["okay", "fine", "normal", "alright"]):
        mood = "okay"
    else:
        mood = "tough"

    msg = random.choice(responses[mood])
    prescription = random.choice(prescriptions)
    love_note = random.choice(love_lines)

    return f"**🎯 {msg}**\n\n**📋 Prescription:** {prescription}\n\n**💕 Love note:** {love_note}"

# --------------------------------------------------
# APP LAYOUT
# --------------------------------------------------
st.title("💙 On-Call Chatbot")

# ECG HEARTBEAT
st.markdown("""
<div class="ecg">
<svg viewBox="0 0 500 100">
  <path d="M0 50 L50 50 L70 20 L90 80 L110 50 L150 50
           L170 30 L190 70 L210 50 L260 50
           L280 20 L300 80 L320 50 L500 50"/>
</svg>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "**From your Golu** ❤️  \n"
    "*Tell me about your day*  \n"
    "**Happy Birthday My Doctor 💕**"
)

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------
if prompt := st.chat_input("How was your day? (good / okay / tough)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --------------------------------------------------
# FLOATING STETHOSCOPE
# --------------------------------------------------
st.markdown('<div class="stethoscope">🩺</div>', unsafe_allow_html=True)
