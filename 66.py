import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menampilkan Deret Kuadrat

def deret_kuadrat():
    batas = int(input("Masukkan batas angka: "))
    for i in range(1, batas + 1):
        print(i ** 2, end=" ")

deret_kuadrat()
