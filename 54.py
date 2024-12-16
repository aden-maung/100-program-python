import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Kalkulator Matriks

def tambah_matriks():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    matriks1 = []
    matriks2 = []
    print("Masukkan elemen matriks pertama:")
    for i in range(baris):
        row = list(map(int, input().split()))
        matriks1.append(row)

    print("Masukkan elemen matriks kedua:")
    for i in range(baris):
        row = list(map(int, input().split()))
        matriks2.append(row)

    hasil = [[matriks1[i][j] + matriks2[i][j] for j in range(kolom)] for i in range(baris)]

    print("Hasil penjumlahan matriks:")
    for row in hasil:
        print(row)

tambah_matriks()
