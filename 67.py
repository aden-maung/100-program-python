import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Luas Lingkaran

import math

def luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * jari_jari ** 2
    print(f"Luas lingkaran adalah: {luas:.2f}")

luas_lingkaran()
