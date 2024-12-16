import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Faktor Bilangan

def cari_faktor():
    angka = int(input("Masukkan angka: "))
    faktor = [i for i in range(1, angka + 1) if angka % i == 0]
    print(f"Faktor-faktor dari {angka} adalah: {faktor}")

cari_faktor()
