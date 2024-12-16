#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program persegi V2
import os
os.system('cls')

print("-"*40)
print("PROGRAM Persegi".center(40))
print("-"*40)

s = float(input("Masukan sisi: "))

v = lambda s: s**2
lp = lambda s: 6 * (s ** 3)

print(f"VOLUME: {v(s)} cm3")
print(f"Luas Permukaan: {lp(s)} cm2")
