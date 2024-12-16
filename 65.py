import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Konversi Suhu (Celsius ke Fahrenheit)

def konversi_suhu():
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Suhu dalam Fahrenheit: {fahrenheit}°F")

konversi_suhu()
