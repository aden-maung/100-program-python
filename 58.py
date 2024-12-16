import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menampilkan Tabel Perkalian

def tabel_perkalian():
    angka = int(input("Masukkan angka untuk tabel perkalian: "))
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")

tabel_perkalian()
