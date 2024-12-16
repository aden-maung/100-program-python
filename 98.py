import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menyusun Deret Aritmatika

def deret_aritmatika():
    a = int(input("Masukkan nilai awal deret (a): "))
    b = int(input("Masukkan beda deret (b): "))
    n = int(input("Masukkan jumlah suku deret (n): "))

    deret = [a + b * i for i in range(n)]
    print("Deret Aritmatika:", deret)

deret_aritmatika()
