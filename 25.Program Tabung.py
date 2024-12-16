#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Russian Roulette
import os
os.system('cls')


print("="*40)
print("PROGRAM TABUNG".center(40))
print("="*40)

r = float(input("masukan jari jari: "))
t = float(input("masukan tinggi: "))

v = lambda r,t: 3.14 * r**2 * t
lp = lambda r,t: (2 * 3.14 * r * t) + (2 * (2 * 3.14 * r))

print(f"VOLUME: {v(r,t)} cm3")
print(f"Luas Permukaan: {lp(r,t)} cm2")