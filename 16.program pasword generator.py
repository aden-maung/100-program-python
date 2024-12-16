#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program pasword generator
import os
os.system ('cls')
import random

print("="*40)
print("PROGRAM PASWORD GENERATOR".center(40))
print("="*40)

choice = str(input("Pin Atau Sandi?? "))

if choice == "pin":
    digit = int(input("Masukan Panjang Digit pin 1-10:"))
    pin_sample = "0123456789"
    pin = "".join(random.sample(pin_sample,digit ))
    print("Pin nya adalah: ", pin)

elif choice == "sandi":
    digit = int(input("Masukan Panjang Digit sandi 1-20:"))
    sandi_sample ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sandi = "".join(random.sample(sandi_sample,digit ))
    print(" sandi nya adalah: ", sandi)

else:
    print("input invalid!")