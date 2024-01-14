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
    ['how can you help me ?',
     'how you can do that ?',]
)
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': 'i can classify documents for you'},
     {'type': 'normal', 'data': 'load a csv file and select the data from columns'},]
)
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

def clear_session() -> None:
    """
    Clears session state variables 'prompts' and 'generated'.
    """
    st.session_state.prompts = []
    st.session_state.generated = []

def main() -> None:
    """
    Initializes the session state variables 'prompts' and
    'generated', sets up the layout using streamlit columns,
    and creates a file uploader. It also creates an empty
    chat placeholder, a button to clear messages, and an
    input field for the user to enter their messages.
    """
    load_main_header()

    st.sidebar.multiselect(
        "Dataframe column",
        ("text", "summary", "title", "body"),
        key="columns"
    )

    st.button("Clear message", on_click=clear_session)

    chat_placeholder = st.empty()

    input_text = st.chat_input('User Input')

    if input_text is not None:
        clear_session()
        st.session_state.prompts.append(input_text)
        st.session_state.generated.append({'type': 'user', 'data': input_text})

    with chat_placeholder.container():
        for i, prompt in enumerate(st.session_state.prompts):
            time.sleep(.5)
            print(prompt)
            message(prompt, is_user=True)
            message(st.session_state.generated[i]['data'])


if __name__ == "__main__":
    main()
