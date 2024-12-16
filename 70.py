import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Tebak Kata

def tebak_kata():
    kata_rahasia = "python"
    tebakan = input("Tebak kata yang saya pikirkan (Hint: Bahasa pemrograman): ").lower()
    if tebakan == kata_rahasia:
        print("Selamat! Kamu menebak dengan benar.")
    else:
        print(f"Sayang sekali, kata yang benar adalah '{kata_rahasia}'.")

tebak_kata()
