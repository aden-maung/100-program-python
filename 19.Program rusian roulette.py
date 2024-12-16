#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Russian Roulette
import os
os.system ('cls')
import random
import time

print(60*("="))
print("Selamat datang di program russian roulette".center(60))
print(60*("="))

def rusian_roulette():
    print("Welcome Soldier")
    peluru = [0, 0, 0, 0, 0, 1]
    random.shuffle(peluru)
    print("Start The Game")
    time.sleep(0.5)
    player_turn = True

    while True:
        if player_turn:
            input("Tekan ENTER untuk menembak....")
            time.sleep(0.7)
            bullet = peluru.pop()
            if bullet == 1:
                print("DOR! Anda tertembak. Game Over.")
                break

            else:
                print("*Click* Anda Berhasil Selamat Kali Ini")
        else:
            print("Giliran Lawan")
            time.sleep(0.7)
            bullet = peluru.pop()
        
            if bullet == 1:
                print("DOR!. Selamat Lawan Tertembak. Anda Menang.")

                break
            else:
                print("*CLICK* Lawan anda selamat kali ini")
        player_turn = not player_turn

        if len(peluru) == 0:
            print("Peluru Revolver kosong. Tidak ada yang tertembak. kalian selamat.")
            break

rusian_roulette()


