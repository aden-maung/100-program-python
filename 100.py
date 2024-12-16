import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Permutasi dan Kombinasi

import math

def permutasi():
    n = int(input("Masukkan jumlah total objek (n): "))
    r = int(input("Masukkan jumlah objek yang dipilih (r): "))
    result = math.perm(n, r)
    print(f"Permutasi ({n}P{r}) adalah: {result}")

def kombinasi():
    n = int(input("Masukkan jumlah total objek (n): "))
    r = int(input("Masukkan jumlah objek yang dipilih (r): "))
    result = math.comb(n, r)
    print(f"Kombinasi ({n}C{r}) adalah: {result}")

def main():
    print("Pilih operasi:")
    print("1. Permutasi")
    print("2. Kombinasi")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        permutasi()
    elif choice == '2':
        kombinasi()
    else:
        print("Pilihan tidak valid")

main()
