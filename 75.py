import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Membalik Urutan Daftar

def balik_daftar():
    daftar = list(map(int, input("Masukkan daftar angka (pisahkan dengan spasi): ").split()))
    print(f"Daftar setelah dibalik: {daftar[::-1]}")

balik_daftar()
