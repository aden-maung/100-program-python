import os
os.system('cls')
import random

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 10/11/2024
#Ini Adalah Program Lempar Dadu V2

print(60*"=")
print("PROGRAM LEMPAR DADU V2".center(60))
print(60*"=")

def gambar_dadu(hasil):
    dadu = {
        1: (
            "┌─────┐",
            "│     │",
            "│  ●  │",
            "│     │",
            "└─────┘"
        ),
        2: (
            "┌─────┐",
            "│ ●   │",
            "│     │",
            "│   ● │",
            "└─────┘"
        ),
        3: (
            "┌─────┐",
            "│ ●   │",
            "│  ●  │",
            "│   ● │",
            "└─────┘"
        ),
        4: (
            "┌─────┐",
            "│ ● ● │",
            "│     │",
            "│ ● ● │",
            "└─────┘"
        ),
        5: (
            "┌─────┐",
            "│ ● ● │",
            "│  ●  │",
            "│ ● ● │",
            "└─────┘"
        ),
        6: (
            "┌─────┐",
            "│ ● ● │",
            "│ ● ● │",
            "│ ● ● │",
            "└─────┘"
        )
    }
    for line in dadu[hasil]:
        print(line)

def lempar_dadu():
    hasil = random.randint(1,6)
    input("Tekan ENTER untuk melempar dadu...")
    gambar_dadu(hasil) 

lempar_dadu()
