import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Penghitung Rata-Rata Nilai

def rata_rata_nilai():
    nilai = list(map(int, input("Masukkan nilai (pisahkan dengan spasi): ").split()))
    rata_rata = sum(nilai) / len(nilai)
    print(f"Rata-rata nilai adalah: {rata_rata}")

rata_rata_nilai()
