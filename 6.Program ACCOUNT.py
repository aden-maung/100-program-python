#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program ACCOUNT
import os
os.system ('cls')
import random

print("="*40)
print("PROGRAM ACCOUNT".center(40))
print("="*40)

input_username = input('masukan username: ')
input_pasword = input('masukan pasword: ')

def login():
    USERNAME = 'aden'
    PASWORD = '12345678'

    if USERNAME == input_username and PASWORD == input_pasword:
        print ("Welcome To The System")

    elif USERNAME == input_username and PASWORD != input_pasword:
        print("pasword invalid")

    elif USERNAME != input_username and PASWORD == input_pasword:
        print("username tidak tersedia")

    else:
        print ("invalid input")

login()
