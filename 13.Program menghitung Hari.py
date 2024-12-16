#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Menghitung Hari
import os
os.system('cls')

print("-"*40)
print("PROGRAM MENGHITUNG HARI".center(40))
print("-"*40)



TAHUN = 365
BULAN = 30
hari = int(input("Masukan Hari: "))
tahun = int(hari / TAHUN)
hari = hari % TAHUN
bulan = int(hari / BULAN)
hari = hari % BULAN

print(tahun , ' tahun ', bulan, ' bulan ', hari, 'hari')