import streamlit as st

def login_page():
    st.title("Login Page")

    # Hardcoded username and password (for demo purposes)
    valid_username = "user123"
    valid_password = "password123"

    # User inputs
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if username == valid_username and password == valid_password:
            st.success("Login successful!")
            # Add further logic for redirection or additional actions after successful login
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login_page()
