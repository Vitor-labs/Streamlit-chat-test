"""
This module builds the interface for the app with components
"""
import pandas as pd
import streamlit as st


def load_main_header() -> None:
    """
    This method loads the main header of the app
    """
    col1, col2, col3 = st.columns([2,1,3])

    with col1:
        st.title("Chatbot💬")
        st.caption("🚀 A chatbot powered by OpenAI LLM")

    with col2:
        st.metric('Total Rows', 232120, "10%", delta_color="inverse")

    with col3:
        uploader = st.file_uploader("Upload a CSV", type=["csv"])

        if uploader is not None:
            st.session_state.labels = list(pd.read_csv(uploader).columns)
        else:
            st.session_state.labels = ['none','file','loaded','yet']

    with st.sidebar:
        st.text_input("OpenAI API Key",type="password")
        st.caption("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        st.divider()

        st.multiselect(
            label="Dataframe column",
            options=st.session_state.labels,
        )