import streamlit as st
email = st.text_input('enter email')
password = st.text_input('enter password')
gender = st.selectbox('Select gender',['male','female','others'])
btn = st.button('Please login')
if btn: #if the button is clicked
    if email == 'saimai@iitbhilai.ac.in' and password == '1234':
        # st.success('Login Successful')
        st.balloons()
        st.write(gender)
    else:
        st.success('login failed')

