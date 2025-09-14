import streamlit as st
from utils import verify_user

def login_page():
    st.markdown("<h2 style='text-align: center;'>Hi! I'm Jon, AI Interviewer</h2>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Login Back to Your Account!")

    with st.form(key='login_form'):
        username = st.text_input("Username / Email", placeholder="Enter your username or email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        handle_jon_login(username, password)


def handle_college_user_login(selected_college, username, password, colleges):
    db_name = next((db for name, db in colleges if name == selected_college), None)

    if db_name and verify_college_user(username, password, db_name):
        conn = connect_college_db(db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT user_type, username FROM users WHERE username = ? OR email = ?", (username, username))
        result = cursor.fetchone()

        if result:
            user_type, corresponding_username = result
            st.session_state['username'] = corresponding_username
        else:
            cursor.execute("SELECT std_username FROM std_users WHERE std_username = ? OR email = ?", (username, username))
            std_user_result = cursor.fetchone()

            if std_user_result:
                corresponding_username = std_user_result[0]
                user_type = 'user'
                st.session_state['username'] = corresponding_username 
            else:
                user_type = None

        if user_type:
            st.session_state['logged_in'] = True
            st.session_state['user_type'] = user_type
            st.success(f"Login successful! Logged in as {user_type}.")
        else:
            st.error("Something went wrong. Please contact your institution’s support.")

        conn.close()
        st.rerun()

    else:
        st.error("Invalid credentials. Please try again.")
