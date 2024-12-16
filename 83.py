import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menentukan Angka Prima

def cek_angka_prima():
    angka = int(input("Masukkan angka: "))
    if angka <= 1:
        print(f"{angka} bukan angka prima.")
    else:
        for i in range(2, angka):
            if angka % i == 0:
                print(f"{angka} bukan angka prima.")
                break
        else:
            print(f"{angka} adalah angka prima.")

cek_angka_prima()
