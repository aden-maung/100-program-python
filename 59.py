import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Faktorial

def hitung_faktorial():
    n = int(input("Masukkan angka untuk dihitung faktorialnya: "))
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    print(f"Faktorial dari {n} adalah {hasil}")

hitung_faktorial()
