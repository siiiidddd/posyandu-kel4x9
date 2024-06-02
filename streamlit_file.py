import streamlit as st

st.title('Posyandu Balita Bunda:family:')
st.write("Posyandu merupakan kependekan dari Pos Pelayanan Terpadu, merupakan Lembaga Kemasyarakatan Desa/Kelurahan (LKD/LKK) sebagai wadah partisipasi masyarakat yang bertugas membantu Kepala Desa/Lurah dalam peningkatan pelayanan social dasar termasuk bidang kesehatan.")
st.write("5 langkah pelayanan pada Posyandu, yaitu:")
st.write("Pendaftaran")
st.write("Pengukuran dan Penimbangan")
st.write("Pencatatan")
st.write("Penyuluhan Kesehatan")
st.header("Aplikasi pendeteksi kurang gizi pada anak dibawah 1 tahun:sparkling_heart:")
st.write("Jika setelah klik tombol selanjutnya lalu tidak muncul keterangan gizi kurang atau lebih berarti gizi anak telah tercukupi")
#KAMI CINTA INFORMATIKA
umur = st.number_input("Masukan umur anak(bulan)= ", 0)
berat = st.number_input("Masukan berat anak=", 0)
lanjut = st.button("Selanjutnya")

if lanjut and umur == 1  and berat < 3:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 1 and berat > 5:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 2 and berat < 4:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 2 and berat > 6:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 3 and berat < 4:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 3 and berat > 7:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 4 and berat < 5:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 4 and berat > 7.5:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 5 and berat < 6:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 5 and berat > 8:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 6 and berat < 6:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 6 and berat > 8:
     st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 7 and berat < 6:
     st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 7 and berat > 9:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 8 and berat < 6.5:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 8 and berat > 9:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 9 and berat < 7:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 9 and berat > 9: 
     st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 10 and berat < 7:
    st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 10 and berat > 10:
    st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 11 and berat < 7:
     st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 11 and berat > 10:
     st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 12 and berat < 7:
     st.write("Berdasarkan umur serta berat badan yang sudah di input maka anak anda mengalami gejala kurang gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
elif lanjut and umur == 12 and berat > 10.5:
     st.write("Berdasarkan umur serta berat badan yang sudah di input, maka anak anda mengalami gejala kelebihan gizi, silahkan periksakan lebih lanjut pada saat pelaksanaan posyandu")
