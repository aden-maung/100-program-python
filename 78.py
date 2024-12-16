import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Volume Bola

import math

def volume_bola():
    jari_jari = float(input("Masukkan jari-jari bola: "))
    volume = (4/3) * math.pi * (jari_jari ** 3)
    print(f"Volume bola adalah: {volume:.2f}")

volume_bola()
