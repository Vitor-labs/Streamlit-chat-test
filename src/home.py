"""
This module defines the main page for the app
"""
import time
import streamlit as st
from streamlit_chat import message

from drives.utils.components import load_main_header


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
    [{'type': 'exemple', 'data': 'i can classify documents for you'},
     {'type': 'exemple', 'data': 'load a csv file and select the data from columns'},]
)
def clear_exemple() -> None:
    """
    Clears session state variables 'prompts' and 'generated'.
    """
    for item in st.session_state.generated:
        if item['type'] == 'exemple':
            st.session_state.prompts = []
            st.session_state.generated = []
            break


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

    st.button("Clear message", on_click=clear_session)

    chat_placeholder = st.empty()

    input_text = st.chat_input('User Input')

    if input_text is not None:
        clear_exemple()
        st.session_state.prompts.append(input_text)
        st.session_state.generated.append({'type': 'user', 'data': input_text})

    with chat_placeholder.container():
        for i, prompt in enumerate(st.session_state.prompts):
            time.sleep(.25)
            message(prompt, is_user=True)
            message(st.session_state.generated[i]['data'])


if __name__ == "__main__":
    main()
