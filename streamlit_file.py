import streamlit as st

st.write('hello world')
umur = st.number_input("Masukan umur= ", 0)
st.button("usia")
st.write("Umur=",umur)