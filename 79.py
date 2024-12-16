import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Angka Terendah

def angka_terendah():
    angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))
    print(f"Angka terendah adalah: {min(angka)}")

angka_terendah()
