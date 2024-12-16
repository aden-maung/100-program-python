import random
import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Roulette

numbers = [
    (32, 'red'), (15, 'black'), (19, 'red'), (4, 'black'), (21, 'red'),
    (2, 'black'), (25, 'red'), (17, 'black'), (34, 'red'), (6, 'black'),
    (27, 'red'), (13, 'black'), (36, 'red'), (11, 'black'), (30, 'red'),
    (8, 'black'), (23, 'red'), (10, 'black'), (5, 'red'), (24, 'black'),
    (16, 'red'), (33, 'black'), (1, 'red'), (20, 'black'), (14, 'red'),
    (31, 'black'), (9, 'red'), (22, 'black'), (18, 'red'), (29, 'black'),
    (7, 'red'), (28, 'black'), (12, 'red'), (35, 'black'), (3, 'red'), (26, 'black')
]

def spin_wheel():
    result = random.choice(numbers)
    return result

def play_roulette():
    print("Selamat datang di permainan Roulette!")
    
    print("Jenis taruhan yang tersedia:")
    print("1. Taruhan pada angka (1-36)")
    print("2. Taruhan pada warna (red / black)")
    bet_type = input("Pilih jenis taruhan (1 atau 2): ").strip()

    if bet_type == '1':
        bet_number = int(input("Masukkan nomor taruhan (1-36): "))
        while bet_number < 1 or bet_number > 36:
            bet_number = int(input("Nomor tidak valid. Masukkan nomor taruhan antara 1-36: "))
        bet = 'number'
    elif bet_type == '2':
        bet_color = input("Masukkan warna taruhan (red/black): ").strip().lower()
        while bet_color not in ['red', 'black']:
            bet_color = input("Warna tidak valid. Masukkan 'red' atau 'black': ").strip().lower()
        bet = 'color'
    else:
        print("Pilihan tidak valid!")
        return

    result = spin_wheel()
    winning_number, winning_color = result

    print(f"\nHasil putaran roulette: {winning_number} ({winning_color})")

    if bet == 'number' and bet_number == winning_number:
        print("Selamat! Anda menang dengan taruhan angka!")
    elif bet == 'color' and bet_color == winning_color:
        print("Selamat! Anda menang dengan taruhan warna!")
    else:
        print("Sayang sekali, Anda kalah. Cobalah lagi!")

if __name__ == "__main__":
    play_roulette()
