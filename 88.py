import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Membuat Pola Bintang Persegi

def persegi_bintang():
    ukuran = int(input("Masukkan ukuran persegi: "))
    for i in range(ukuran):
        print("*" * ukuran)

persegi_bintang()
