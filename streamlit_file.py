import streamlit as st

st.write('hello world')
anak = st.text_input("Masukan nama anak=")
ortu = st.text_input("Masukan nama orang tua=")
umur = st.number_input("Masukan umur anak= ", 0)
tinggi = st.number_input("Masukan tinggi anak=", 0)
berat = st.number_input("Masukan berat anak=", 0)
selanjutnya = st.button("lanjut")
if selanjutnya :
    sidan = 1 * umur
    st.write("Umur=",sidan)