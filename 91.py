import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Luas Trapesium

def luas_trapesium():
    a = float(input("Masukkan panjang sisi sejajar pertama: "))
    b = float(input("Masukkan panjang sisi sejajar kedua: "))
    t = float(input("Masukkan tinggi trapesium: "))
    luas = 0.5 * (a + b) * t
    print(f"Luas trapesium adalah: {luas}")

luas_trapesium()
