import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Cek Genap atau Ganjil

def cek_genap_atau_ganjil():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap.")
    else:
        print(f"{angka} adalah angka ganjil.")

cek_genap_atau_ganjil()
