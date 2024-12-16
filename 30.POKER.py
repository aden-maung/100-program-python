import os
os.system('cls')
import random

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 10/11/2024
#Ini Adalah Program Poker

print(60*"=")
print("PROGRAM POKER".center(60))
print(60*"=")

# Membuat setumpuk kartu (angka dan jenis)
def buat_deck():
    angka = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    jenis = ['♠', '♥', '♦', '♣']
    deck = [f'{a}{j}' for a in angka for j in jenis]
    random.shuffle(deck)
    return deck

# Membagikan kartu kepada pemain
def bagikan_kartu(deck, jumlah_pemain=2, kartu_per_pemain=2):
    tangan_pemain = []
    for _ in range(jumlah_pemain):
        tangan_pemain.append([deck.pop() for _ in range(kartu_per_pemain)])
    return tangan_pemain

# Menampilkan kartu pemain
def tampilkan_kartu(tangan_pemain):
    for i, tangan in enumerate(tangan_pemain, 1):
        print(f"Pemain {i}: {', '.join(tangan)}")

# Program utama
def main():
    deck = buat_deck()
    jumlah_pemain = 2
    tangan_pemain = bagikan_kartu(deck, jumlah_pemain)
    tampilkan_kartu(tangan_pemain)

main()