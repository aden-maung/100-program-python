import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Konversi Desimal ke Biner

def desimal_ke_biner():
    desimal = int(input("Masukkan angka desimal: "))
    biner = bin(desimal).replace("0b", "")
    print(f"Angka biner: {biner}")

desimal_ke_biner()
