import streamlit as st
import streamlit_authenticator as stauth

# ----- USER CONFIGURATION -----
# Define users and hashed passwords
names = ['Iqra']
usernames = ['iqra22']
# Hashed password for: iqra123
hashed_passwords = stauth.Hasher(['iqra123']).generate()

# Create authenticator object
authenticator = stauth.Authenticate(
    credentials={
        'usernames': {
            usernames[0]: {
                'name': names[0],
                'password': hashed_passwords[0]
            }
        }
    },
    cookie_name='my_app_cookie',
    key='abcdef',
    cookie_expiry_days=30
)

# ----- LOGIN FORM -----
name, authentication_status, username = authenticator.login('Login', 'main')

# ----- CONDITIONAL RENDERING -----
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.success(f'Welcome {name}!')
    st.title("🔐 Secure Streamlit App")
    
    # ---- MAIN APP CONTENT HERE ----
    st.write("You are now logged in! 🎉")
    st.write("Put your main app functionality here.")
    
elif authentication_status is False:
    st.error('❌ Incorrect username or password.')

elif authentication_status is None:
    st.warning('Please enter your username and password.')
