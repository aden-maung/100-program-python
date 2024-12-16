import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Nilai Faktorial

def faktorial():
    angka = int(input("Masukkan angka: "))
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i
    print(f"Faktorial dari {angka} adalah: {hasil}")

faktorial()
