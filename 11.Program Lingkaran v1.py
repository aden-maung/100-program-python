#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program Lingkaran V2
import os
os.system('cls')

print("="*40)
print("PROGRAM LINGKARAN".center(40))
print("="*40)

r = float(input("masukan jari jari: "))

pi = 3.14
l = lambda r: pi * r**2
k = lambda r,pi :2 * pi * r

print(f"luas = {l(r)} cm2")
print(f"keliling = {k(r,pi)} cm")
