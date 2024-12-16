import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program penghitung kecepatan typing
import time

def kecepatan_ketik():
    kalimat_tantangan = "Saya sedang mengetik dengan cepat!"
    print("Tantangan ketik: " + kalimat_tantangan)
    input("Tekan Enter untuk memulai mengetik...")

    mulai = time.time()
    input("Ketik kalimat di atas dan tekan Enter saat selesai: ")
    selesai = time.time()

    waktu = selesai - mulai
    kecepatan = len(kalimat_tantangan) / waktu * 60  # dalam kata per menit
    print(f"Kecepatan mengetikmu adalah {kecepatan:.2f} karakter per menit!")

kecepatan_ketik()
