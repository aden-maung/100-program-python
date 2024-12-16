import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Mencari Nilai Terbesar dan Terkecil dalam Daftar

def nilai_terbesar_terkecil():
    angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))
    print(f"Nilai terbesar: {max(angka)}")
    print(f"Nilai terkecil: {min(angka)}")

nilai_terbesar_terkecil()
