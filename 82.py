import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Membuat Pola Bintang Segitiga Terbalik

def segitiga_bintang_terbalik():
    baris = int(input("Masukkan jumlah baris: "))
    for i in range(baris, 0, -1):
        print("*" * i)

segitiga_bintang_terbalik()
