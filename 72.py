import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Bilangan Terbesar

def bilangan_terbesar():
    angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))
    print(f"Bilangan terbesar adalah: {max(angka)}")

bilangan_terbesar()
