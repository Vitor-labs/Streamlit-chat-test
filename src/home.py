"""
This module defines the main page for the app
"""
import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def chat_bot_response(input_text:str) -> str:
    """
    this method handles the calling to specific chat
    and it's responses

    Args:
        input_text (str): user prompt

    Returns:
        str: _description_
    """
    # This function could contain logic to generate a response from a chatbot model
    # For demonstration purposes, it echoes the input text
    return f"You said: '{input_text}'"

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.prompts.append(user_input)
    st.session_state.generated.append("The messages from Bot\nWith new line")

def on_btn_click():
    del st.session_state.prompts[:]
    del st.session_state.generated[:]

def main():
    st.session_state.setdefault(
        'prompts', 
        ['Hello there',]
    )
    st.session_state.setdefault(
        'generated', 
        [{'type': 'normal', 'data': 'General kenoby!'},]
    )
    st.title("💬 Chatbot")
    st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

    chat_placeholder = st.empty()

    st.button("Clear message", on_click=on_btn_click)

    with st.container():
        user_input = st.text_area("",on_change=on_input_change,key="user_input")

        if user_input:
            with st.spinner("Thinking..."):
                response = chat_bot_response(user_input)
                idx = len(st.session_state['generated'])

                st.session_state['generated'][idx]['data'] = response
                st.session_state['prompts'][idx] = response
                st.text_area("Bot", value=response, height=200, max_chars=None)

            with chat_placeholder.container():
                for i in range(len(list(st.session_state['generated']))):
                    message(st.session_state['prompts'][i], is_user=True, key=f"{i}_user")
                    message(
                        st.session_state['generated'][i]['data'],
                        key=f"{i}",
                        allow_html=True,
                        is_table=True
                                 if st.session_state['generated'][i]['type']=='table'
                                 else False
                )

if __name__ == "__main__":
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    main()
