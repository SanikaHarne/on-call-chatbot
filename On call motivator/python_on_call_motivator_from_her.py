import streamlit as st
import random

st.set_page_config(page_title="On-Call Chatbot 💙", page_icon="💙", layout="centered")

# Your messages (customize these!)
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

# Chatbot logic
def get_response(message):
    message_lower = message.lower()
    
    if any(word in message_lower for word in ["good", "great", "nice", "awesome", "best"]):
        mood = "good"
    elif any(word in message_lower for word in ["okay", "fine", "normal", "alright"]):
        mood = "okay"
    else:
        mood = "tough"  # default for complaints/anything else
    
    msg = random.choice(responses[mood])
    prescription = random.choice(prescriptions)
    love_note = random.choice(love_lines)
    
    return f"**🎯 {msg}**\n\n**📋 Prescription:** {prescription}\n\n**💕 Love note:** {love_note}"

# App layout
st.title("💙 On-Call Chatbot")
st.markdown("**From your Golu** ❤️ *Tell me about your day:*")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How was your day? (good/okay/tough)"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

