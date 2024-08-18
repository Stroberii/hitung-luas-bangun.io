import streamlit as st
from streamlit_option_menu import option_menu
import math


# navigasi sidebar
with st.sidebar:
    selected = option_menu ('Hitung Luas Bangun',
    ['Hitung Luas Persegi Panjang',
    'Hitung Luas Segitiga',
    'Hitung Luas Lingkaran',
    'Hitung Luas Trapesium'],
    default_index=0)


#halaman hitung luas persegi panjang
if (selected == 'Hitung Luas Persegi Panjang'):
    st.title('Hitung Luas Persegi Panjang')
    
    panjang = st.number_input('Masukan Nilai Panjang', 0)
    lebar = st.number_input('Masukan Nilai Lebar', 0)
    hitung = st.button('Hitung Luas')

    if hitung:
        luas = panjang * lebar
        st.success (f'Luas Persegi Panjang Adalah: {luas}')


#halaman hitung luas segitiga
if (selected == 'Hitung Luas Segitiga'):
    st.title('Hitung Luas Segitiga')

    alas = st.slider ('Masukan Nilai Alas', 0, 100)
    tinggi = st.slider ('Masukan Nilai Tinggi', 0, 100)
    hitung = st.button('Hitung Luas Segitiga')

    if hitung:
        luas = 0.5 * alas * tinggi
        st.success (f'Luas Segitiganya Adalah: {luas}')


#halaman hitung luas lingkaran
if (selected == 'Hitung Luas Lingkaran'):
    st.title('Hitung Luas Lingkaran')

    jari = st.number_input('Masukan Jari-Jari: ', min_value=0)
    pi_3_14 = 3.14
    st.write(f'Nilai π yang digunakan: {pi_3_14}')
    hitung = st.button('Hitung Luas Lingkaran')

    if hitung:
        luas = pi_3_14 * jari**2
        st.success(f'Luas Lingkaran Adalah:  {luas}')


#halaman hitung luas trapesium
if (selected == 'Hitung Luas Trapesium'):
    st.title('Hitung Luas Trapesium')

    alas_a = st.number_input('Masukan Alas A: ', 0)
    alas_b = st.number_input('Masukan Alas B: ', 0)
    tinggi = st.number_input('Masukan Tinggi Trapesium: ', 0)
    hitung = st.button('Hitung Luas Trapesium')

    if hitung:
        luas = 0.5 * (alas_a * alas_b) * tinggi
        st.success(f'Luas Trapesium Adalah: {luas}')