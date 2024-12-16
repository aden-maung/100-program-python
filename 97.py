import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menampilkan Matriks Transpose

def transpose_matriks():
    baris = int(input("Masukkan jumlah baris matriks: "))
    kolom = int(input("Masukkan jumlah kolom matriks: "))
    
    matriks = []
    for i in range(baris):
        row = list(map(int, input(f"Masukkan elemen baris {i+1} (pisahkan dengan spasi): ").split()))
        matriks.append(row)

    print("\nMatriks asli:")
    for row in matriks:
        print(row)

    # Matriks transpose
    transpose = [[matriks[j][i] for j in range(baris)] for i in range(kolom)]

    print("\nMatriks transpose:")
    for row in transpose:
        print(row)

transpose_matriks()
