import streamlit as st

st.title('Posyandu Balita Bunda')
st.header("Aplikasi pendeteksi kurang gizi pada anak dibawah 1 tahun")
st.write("https://ayosehat.kemkes.go.id/posyandu-semakin-siap-melayani-masyarakat-secara-menyuluh-")
st.write("Jika tertulis keterangan 'true' berarti kurang gizi, jika tertulis 'false' maka gizi tidak kurang")

umur = st.number_input("Masukan umur anak(bulan)= ", 0)
tinggi = st.number_input("Masukan tinggi anak=", 0)
berat = st.number_input("Masukan berat anak=", 0)

if umur == 1 :
    berat < 3
    st.write("kurang gizi")
elif umur == 1 :
    berat > 5
elif umur == 2 :
    berat < 5
    st.write("Kurang gizi")
elif umur == 2 :
    berat > 7
    