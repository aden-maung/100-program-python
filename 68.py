import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Rata-Rata

def rata_rata():
    angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))
    rata_rata = sum(angka) / len(angka)
    print(f"Rata-rata angka tersebut adalah: {rata_rata}")

rata_rata()
