import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Kalkulator Matematika dengan Fungsi-fungsi Dasar

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak dapat dibagi dengan nol!"
    else:
        return x / y

def main():
    print("Pilihan operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil: {tambah(num1, num2)}")
    elif pilihan == '2':
        print(f"Hasil: {kurang(num1, num2)}")
    elif pilihan == '3':
        print(f"Hasil: {kali(num1, num2)}")
    elif pilihan == '4':
        print(f"Hasil: {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid")

main()
