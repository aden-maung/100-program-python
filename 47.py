import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program kalkulator tanggal
from datetime import datetime

def hitung_selisih():
    tanggal1 = input("Masukkan tanggal pertama (YYYY-MM-DD): ")
    tanggal2 = input("Masukkan tanggal kedua (YYYY-MM-DD): ")

    t1 = datetime.strptime(tanggal1, "%Y-%m-%d")
    t2 = datetime.strptime(tanggal2, "%Y-%m-%d")
    
    selisih = abs((t2 - t1).days)
    print(f"Selisih hari: {selisih} hari")

hitung_selisih()
