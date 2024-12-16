import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Penghitung Vokal dan Konsonan

def hitung_vokal_konsonan():
    kalimat = input("Masukkan kalimat: ").lower()
    vokal = "aeiou"
    vokal_count = 0
    konsonan_count = 0

    for char in kalimat:
        if char in vokal:
            vokal_count += 1
        elif char.isalpha():
            konsonan_count += 1

    print(f"Jumlah vokal: {vokal_count}")
    print(f"Jumlah konsonan: {konsonan_count}")

hitung_vokal_konsonan()
