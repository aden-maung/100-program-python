#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program Segitiga V2
import os
os.system('cls')

print("="*40)
print("PROGRAM SEGITIGA".center(40))
print("="*40)

tinggi = float(input("masukan tinggi: "))
alas = float(input("masukan alas: "))

luas = lambda alas: alas * tinggi / 2

print(f"Luas : {luas(alas)} cm2")

