import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth


cred = credentials.Certificate("streamlitpondering-e506699f1b52.json")
#run only first time when run app and comment later
firebase_admin.initialize_app(cred)



def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])

    def f():
        if email and password:
            try:
                user  = auth.get_user_by_email(email)
                #print(user.uid)
                st.success('Login success')
            except:
                st.warning('Login failed')

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.button('Login', on_click=f())
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')
        if st.button('Create My Account'):
            user = auth.create_user(email=email, password=password, uid=username)
            st.success('Account created successfully!')
            st.markdown('Please, login with your email and password')
            st.balloons()