import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program menghitung huruf
from collections import Counter

def hitung_huruf():
    kalimat = input("Masukkan kalimat: ")
    huruf = [h for h in kalimat.lower() if h.isalpha()]
    penghitung = Counter(huruf)
    huruf_terbanyak = penghitung.most_common(1)
    
    if huruf_terbanyak:
        print(f"Huruf yang paling banyak muncul adalah '{huruf_terbanyak[0][0]}' dengan jumlah {huruf_terbanyak[0][1]} kali.")
    else:
        print("Tidak ada huruf dalam kalimat.")

hitung_huruf()
