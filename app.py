import streamlit as st
from rag import load_rag

st.title("📄 PDF Chatbot (Local RAG)")

if "qa" not in st.session_state:
    if st.button("Load PDF"):
        st.session_state.qa = load_rag("data/DATA MODELING.pdf")
        st.success("PDF loaded!")

question = st.text_input("Ask a question")

if question and "qa" in st.session_state:
    answer = st.session_state.qa.run(question)
    st.write("### Answer")
    st.write(answer)
