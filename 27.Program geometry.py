#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Geometry
import os
import math
os.system ('cls')

print(60*"=")
print("PROGRAM PERHITUNGAN GEOMETRI".center(60))
print(60*"=")

#Fungsi Perhitungan Lingkaran
def perhitungan_lingkaran():
    radius = float(input("Masukan Jari-Jari Lingkaran: "))
    luas = lambda r: math.pi * r ** 2
    keliling = lambda r: 2 * math.pi * r
    print(f"Luas LIngkaran Nya Adalah: {luas(radius):.2f}")
    print(f"Keliling lingkaran nya adalah {keliling(radius):.2f}")

#Fungsi Perhitungan Persegi
def perhitungan_persegi():
    sisi = float(input("Masukan sisi: "))
    volume = lambda s: s**2
    luas_permukaan = lambda s: 6 * (s ** 3)
    print(f"Luas permukaan kubus adalah: {luas_permukaan(sisi):.2f}")
    print(f"Volume kubus adalah: {volume(sisi):.2f}")

#Fungsi Perhitungan Kubus
def perhitungan_kubus():
    jari_jari = float(input("Masukan jari-jari kubus: "))
    luas = lambda r: math.pi * r ** 2
    keliling = lambda r:2 * math.pi * r
    print(f"Luas kubus adalah: {luas(jari_jari):.2f}")
    print(f"Keliling kubus adalah: {keliling(jari_jari):.2f}")

#Fungsi Perhitungan Tabung
def perhitungan_tabung():
    r = float(input("masukan jari jari: "))
    t = float(input("masukan tinggi: "))
    volume= lambda r,t: 3.14 * r**2 * t
    luas_permukaan = lambda r,t: (2 * 3.14 * r * t) + (2 * (2 * 3.14 * r))
    print(f"Volume tabung adalah: {volume(r,t):.2f}")
    print(f"Luas permukaan tabung adalah: {luas_permukaan(r,t):.2f}")

#Fungsi Perhitungan Segitiga
def perhitungan_Segitiga():
    tinggi = float(input("masukan tinggi: "))
    alas = float(input("masukan alas: "))
    luas = lambda alas: alas * tinggi / 2
    print(f"Luas : {luas(alas):.2f}")

#main input untuk menjalankan program
def main():
    while True:
        print(60*"=")
        print("\nPilih geometri yang ingin di hitung: ")
        print("""
              1.Lingkaran
              2.Persegi 
              3.Kubus
              4.Tabung
              5.Segitiga""".center(60).capitalize())
        choice = int(input("Masukan Input dari 1-5: "))
        
        print(60*"=")
        if choice == 1:
            perhitungan_lingkaran()
            print("Terimakasih sudah menggunakan Program ini")
            break 
        elif choice == 2:
            perhitungan_persegi()
            print("Terimakasih sudah menggunakan Program ini")
            break 
        elif choice == 3:
            perhitungan_kubus()
            print("Terimakasih sudah menggunakan Program ini")
            break 
        elif choice == 4:
            perhitungan_tabung()
            print("Terimakasih sudah menggunakan Program ini")
            break 
        elif choice == 5:
            perhitungan_Segitiga()  
            print("Terimakasih sudah menggunakan Program ini")
            break 
        else:
            print("Input yang anda masukan invalid, silahkan coba kembali")
#Fungsi untuk memanggil Input
if __name__ == "__main__":
    main()