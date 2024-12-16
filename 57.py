import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Palindrome Checker

def cek_palindrome():
    teks = input("Masukkan kata atau kalimat: ").replace(" ", "").lower()
    if teks == teks[::-1]:
        print("Ya, ini adalah palindrome!")
    else:
        print("Bukan palindrome!")

cek_palindrome()
