
import yaml
from yaml.loader import SafeLoader

import streamlit as st
import streamlit_authenticator as stauth

def handle_user_login() -> None:
    """
    Handles user login by reading user credentials from a
    YAML file, authenticating the user, and displaying
    appropriate messages based on the authentication status.

    TODO: need to implement loging logic
    """
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

        if st.session_state["authentication_status"]: # authenticated
            authenticator.logout('Logout', 'main', key='unique_key')
            st.write(f'Welcome *{st.session_state["username"]}*')
        elif st.session_state["authentication_status"] is False: # incorrect
            st.error('Username/password is incorrect')
            authenticator.register_user('Register user', 'sidebar')
        elif st.session_state["authentication_status"] is None: # not logged in
            st.warning('Please enter your username and password')
