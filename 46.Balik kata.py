import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Roulette
def balik_kata():
    kalimat = input("Masukkan kalimat: ")
    kata = kalimat.split()
    kata_terbalik = " ".join(kata[::-1])
    print(f"Kalimat terbalik: {kata_terbalik}")

balik_kata()
