import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung GCD (Greatest Common Divisor)

import math

def gcd_angka():
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    gcd = math.gcd(a, b)
    print(f"Pembagi terbesar bersama (GCD) dari {a} dan {b} adalah: {gcd}")

gcd_angka()
