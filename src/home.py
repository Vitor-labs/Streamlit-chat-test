"""
This module defines the main page for the app
"""
import time
import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="Labeler Chat",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.session_state.setdefault(
    'prompts', 
    ['Hello there',
    'how can you help me ?',]
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': 'General kenoby!'},
     {'type': 'normal', 'data': 'i can classify documents for you'}]
)

def on_btn_click() -> None:
    """
    Clears session state variables 'prompts' and 'generated'.
    """
    del st.session_state.prompts
    del st.session_state.generated

def main():
    """
    Initializes the session state variables 'prompts' and
    'generated', sets up the layout using streamlit columns,
    and creates a file uploader. It also creates an empty
    chat placeholder, a button to clear messages, and an
    input field for the user to enter their messages.
    """
    col1, col2, col3 = st.columns([2,1,3])

    with col1:
        st.title("Chatbot💬")
        st.caption("🚀 A chatbot powered by OpenAI LLM")

    with col2:
        st.metric('Total Rows', 232120, "10%", delta_color="inverse")

    with col3:
        file = st.file_uploader("Upload a CSV", type=["csv"])

    chat_placeholder = st.empty()

    with chat_placeholder.container():
        for i, _ in enumerate(st.session_state.prompts):
            message(st.session_state.prompts[i], is_user=True)
            message(st.session_state.generated[i]['data'])
            time.sleep(1)

    st.button("Clear message", on_click=on_btn_click)

    input_text = str(st.chat_input('User Input'))

    st.session_state['generated'].append({'type':'normal', 'data':input_text})
    st.session_state['prompts'].append(input_text)


if __name__ == "__main__":
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

        #select dataframe colomn
        st.selectbox(
            "Dataframe column",
            ("text", "summary", "title", "body"),
        )
    main()
