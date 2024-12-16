#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program Segi Panjang V2
import os
os.system('cls')


print("-"*50)
print("PROGRAM SEGI PANJANG".center(50))
print("-"*50)

p = float(input("Masukan Panjang: "))
l = float(input("Masukan Lebar: "))

lu = lambda p: p * l
k = lambda p,l : 2 * p + l

print(f"Luas: {lu(p)} cm")
print(f"keiling: {k(p,l)} cm2")
