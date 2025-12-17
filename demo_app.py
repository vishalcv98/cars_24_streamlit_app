import streamlit as st

def sqr(num):
    return num*num


num = st.number_input("Enter a number", value=0)

if st.button("Calculate the square"):
    result = sqr(num)
    st.write(f"The square of {num} is {result}")

