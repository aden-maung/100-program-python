import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Menghitung Jumlah Angka Genap dan Ganjil

def hitung_genap_ganjil():
    angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))
    genap = sum(1 for x in angka if x % 2 == 0)
    ganjil = sum(1 for x in angka if x % 2 != 0)
    print(f"Jumlah angka genap: {genap}")
    print(f"Jumlah angka ganjil: {ganjil}")

hitung_genap_ganjil()
