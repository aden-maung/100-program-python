
#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program tebak angka
import os
os.system ('cls')
import random

n = random.randrange(1,10)

guess = int(input("Tebak Angka: "))
while n!= guess: 
    
    if guess < n:
        print("dingin")
        
        guess = int(input("Masukin Nomor Lagi: "))
    
    elif guess > n:
        print("panas")
        
        guess = int(input("Masukin Nomor Lagi: "))
    
    else:
        break
print("GELOOO BENER CUYY!!")
print('Makasih Sudah Mencoba:)')