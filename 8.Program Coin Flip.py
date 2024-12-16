#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program coin flip
import random
import os
os.system('cls')

print(30*("="))
print("Selamat datang di program coin flip")
print(30*("="))

side = random.randint(1,2)
coin = [1 =="Heads", 2 == "Tails"]
choice = int(input("Please chose a side of coin: "))
if choice == side and side == 1:
     print("It's Heads You win!!")
elif choice == side and side == 2:
    print("it's Tails You Win!!")
else:
    print("You lose")
