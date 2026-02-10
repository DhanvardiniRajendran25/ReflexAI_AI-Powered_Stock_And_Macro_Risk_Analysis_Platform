import streamlit as st
from rag_interface import SorosRAGChatbot
import re

# Page configuration
st.set_page_config(
    page_title="Soros AI Chatbot",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Soros-themed styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        background-color: #1e2530;
        color: #ffffff;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #1e3a5f;
        border-left: 4px solid #4a90e2;
    }
    .bot-message {
        background-color: #1e2530;
        border-left: 4px solid #d4af37;
    }
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #d4af37;
    }
    .stButton > button {
        background-color: #d4af37;
        color: #000000;
        font-weight: bold;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 0.3rem;
    }
    .stButton > button:hover {
        background-color: #b8941f;
    }
    h1 {
        color: #d4af37;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .subtitle {
        text-align: center;
        color: #a0a0a0;
        font-style: italic;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

def extract_direct_answer(full_response: str) -> str:
    """
    Extract only the 'Direct Answer' section from the full response.
    """
    # Try to find the Direct Answer section
    pattern = r"1\.\s*Direct Answer\s*[:\n]+(.*?)(?=\n\s*2\.|$)"
    match = re.search(pattern, full_response, re.DOTALL | re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    
    # Fallback: if pattern doesn't match, return first paragraph
    lines = full_response.split('\n')
    for i, line in enumerate(lines):
        if 'direct answer' in line.lower():
            # Get content after this line until next numbered section
            answer_lines = []
            for j in range(i+1, len(lines)):
                if re.match(r'^\s*\d+\.', lines[j]):
                    break
                answer_lines.append(lines[j])
            if answer_lines:
                return '\n'.join(answer_lines).strip()
    
    # Last resort: return first substantial paragraph
    paragraphs = [p.strip() for p in full_response.split('\n\n') if p.strip()]
    return paragraphs[0] if paragraphs else full_response

# Initialize session state
if 'chatbot' not in st.session_state:
    with st.spinner('Initializing Soros AI Chatbot...'):
        st.session_state.chatbot = SorosRAGChatbot()
    st.session_state.messages = []

# Header
st.markdown("<h1>💼 George Soros AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore investment philosophy through the lens of George Soros</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x200/1e2530/d4af37?text=Soros+AI", use_container_width=True)
    st.markdown("### About")
    st.info(
        "This chatbot provides educational insights inspired by George Soros's "
        "investment philosophy, including reflexivity, market psychology, and macro analysis. "
        "\n\n**Note:** This is NOT financial advice."
    )
    
    st.markdown("### Features")
    st.markdown("""
    - 📚 RAG-based knowledge retrieval
    - 🧠 Soros-style reasoning
    - 📊 Market context awareness
    - 💡 Educational insights
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-header">You</div>
                <div>{message["content"]}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="message-header">Soros AI</div>
                <div>{message["content"]}</div>
            </div>
        """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Ask about trading, investing, markets, or Soros's philosophy...")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message immediately
    st.markdown(f"""
        <div class="chat-message user-message">
            <div class="message-header">You</div>
            <div>{user_input}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Get bot response
    with st.spinner('Thinking like Soros...'):
        full_response = st.session_state.chatbot.answer(user_input)
        direct_answer = extract_direct_answer(full_response)
    
    # Add bot response to chat
    st.session_state.messages.append({"role": "assistant", "content": direct_answer})
    
    # Display bot response
    st.markdown(f"""
        <div class="chat-message bot-message">
            <div class="message-header">Soros AI</div>
            <div>{direct_answer}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Rerun to update the chat display
    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Powered by RAG + Gemini AI | Educational purposes only</p>",
    unsafe_allow_html=True
)
