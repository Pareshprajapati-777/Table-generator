import streamlit as st
# python -m streamlit run table.py
st.title("Welcome to Table World")
n= st.number_input("Enter a number", min_value=0,max_value=1000)
if st.button("Submit"):
    for i in range(1,11):
        st.write(f"{n} * {i} = {n*i}")
    