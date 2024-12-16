import os 
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Tebak Angka (Dengan Petunjuk)

import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    while True:
        tebakan = int(input("Masukkan tebakanmu (1-100): "))
        if tebakan < angka_rahasia:
            print("Tebakanmu terlalu rendah, coba lagi!")
        elif tebakan > angka_rahasia:
            print("Tebakanmu terlalu tinggi, coba lagi!")
        else:
            print(f"Selamat! Kamu menebak angka {angka_rahasia} dengan benar!")
            break

tebak_angka()
