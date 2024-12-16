import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Membuat Segitiga Bintang

def segitiga_bintang():
    baris = int(input("Masukkan jumlah baris: "))
    for i in range(1, baris + 1):
        print("*" * i)

segitiga_bintang()
