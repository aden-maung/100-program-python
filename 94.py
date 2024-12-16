import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menentukan Deret Angka Genap

def deret_genap():
    batas = int(input("Masukkan batas angka: "))
    for i in range(2, batas + 1, 2):
        print(i, end=" ")

deret_genap()
