import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Bilangan Prima

def cari_prima():
    batas = int(input("Masukkan batas angka: "))
    for angka in range(2, batas + 1):
        prima = True
        for i in range(2, angka):
            if angka % i == 0:
                prima = False
                break
        if prima:
            print(angka)

cari_prima()
