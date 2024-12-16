#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Menghitung suhu
import os
os.system('cls')

print("="*40)
print("PROGRAM SUHU".center(40))
print("="*40)

c = float(input("Masukan Suhu Dalam Celcius: "))

r = ((4/5) * c)
print("Suhu Dalam Reamur:",r,("r"))

f = (9/5) * c + 32
print("Suhu Dalam Farenheit: ",f,"F")

k = c + 273
print ("Suhu Dalam Kelvin: ",k,"K")