import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menampilkan Angka Fibonacci ke-N

def fibonacci_ke_n():
    n = int(input("Masukkan angka Fibonacci yang ke-N: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci_ke_n()
