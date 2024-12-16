import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Cek Tahun Kabisat

def cek_tahun_kabisat():
    tahun = int(input("Masukkan tahun: "))
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print(f"{tahun} adalah tahun kabisat.")
    else:
        print(f"{tahun} bukan tahun kabisat.")

cek_tahun_kabisat()
