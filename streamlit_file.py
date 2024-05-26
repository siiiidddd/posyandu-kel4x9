import streamlit as st
from PIL import image

st.image('foto posyandu.png')
st.title('Posyandu Balita Bunda')
st.write("Keterangan")

umur = st.number_input("Masukan umur anak= ", 0)
tinggi = st.number_input("Masukan tinggi anak=", 0)
berat = st.number_input("Masukan berat anak=", 0)
selanjutnya = st.button("lanjut")
if selanjutnya :
    berat < 10
    st.write("kurang gizi")
else :
    berat > 10
    st.write("cukup")