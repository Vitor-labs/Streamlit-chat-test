import streamlit as st


def load_main_header():
    """
    Loads the main header of the chatbot interface.
    with title, total rows, and file uploader.
    """
    col1, col2, col3 = st.columns([2,1,3])

    with col1:
        st.title("Chatbot💬")
        st.caption("🚀 A chatbot powered by OpenAI LLM")

    with col2:
        st.metric('Total Rows', 232120, "10%", delta_color="inverse")

    with col3:
        file = st.file_uploader("Upload a CSV", type=["csv"])
