import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Cek Palindrome pada Angka

def cek_palindrome_angka():
    angka = input("Masukkan angka: ")
    if angka == angka[::-1]:
        print("Angka ini adalah palindrome.")
    else:
        print("Angka ini bukan palindrome.")

cek_palindrome_angka()
