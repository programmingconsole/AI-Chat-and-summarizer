import streamlit as st
from ai_utils import generate_summary, generate_questions, chat_with_ai

st.set_page_config(page_title="AI Summary App", layout="centered")

st.title("AI Summary & QnA Generator")

# Input text
text = st.text_area("Enter your text:", height=200)

if st.button("Summarize"):
    if text.strip():
        with st.spinner("Generating summary..."):
            summary = generate_summary(text)
            st.success("Summary Generated:")
            st.write(summary)

if st.button("Generate Questions"):
    if text.strip():
        with st.spinner("Generating questions..."):
            questions = generate_questions(text)
            st.success("Questions Generated:")
            st.write(questions)

# Chat section
st.subheader("Chat with AI")
prompt = st.text_input("Ask me anything:")
if st.button("Send"):
    if prompt.strip():
        with st.spinner("Thinking..."):
            reply = chat_with_ai(prompt)
            st.write(f": {reply}")
