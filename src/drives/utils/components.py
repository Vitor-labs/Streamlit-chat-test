"""
This module builds the interface for the app with components
"""
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth


def load_main_header() -> None:
    """
    This method loads the main header of the app
    """
    col1, col2, col3 = st.columns([2,1,3])

    with col1:
        st.title("Doc Labeler💬")
        st.caption("🚀 A chatbot powered by OpenAI LLM")

    with col2:
        total_rows = st.empty()

    with col3:
        uploader = st.file_uploader("Upload a CSV", type=["csv"])

        if uploader is not None:
            df = pd.read_csv(uploader)
            st.session_state.labels = list(df.columns)
            total_rows.metric('Total Rows', len(df), '10%', "inverse")
        else:
            st.session_state.labels = ['none','file','loaded','yet']

    with st.sidebar:
        tab1, tab2, tab3 = st.tabs(["🔐 Auth", "📝 Config", "✅ saved"])

        with tab1:
            # https://github.com/mkhorasani/Streamlit-Authenticator
            # stauth seems to be easy to implement, lets see other
            # option, if nothing better apear, it'll be the best
            with open('./.streamlit/users.yaml', 'r') as file:
                config = yaml.load(file, Loader=SafeLoader)

            authenticator = stauth.Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized']
            )
            authenticator.login('Login', 'main')

        with tab2:
            st.multiselect(
                label="Dataframe column",
                options=st.session_state.labels,
            )

        with tab3:
            for item in st.session_state.prompts:
                st.button(item, help='select this previous prompt', use_container_width=True)
