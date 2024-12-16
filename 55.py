import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Pencari Kata Terpanjang

def kata_terpanjang():
    kalimat = input("Masukkan kalimat: ")
    kata = kalimat.split()
    terpanjang = max(kata, key=len)
    print(f"Kata terpanjang adalah: {terpanjang}")

kata_terpanjang()
