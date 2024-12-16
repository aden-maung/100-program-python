import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Luas Permukaan Kubus

def luas_permukaan_kubus():
    sisi = float(input("Masukkan panjang sisi kubus: "))
    luas = 6 * (sisi ** 2)
    print(f"Luas permukaan kubus adalah: {luas}")

luas_permukaan_kubus()
