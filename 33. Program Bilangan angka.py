import os
os.system('cls')


#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program Bilangan Angka

def bilangan():
    angka = int(input("Masukan angka: "))

    if angka < 10:
        print(f"{angka} Adalah Bilangan Asli")

    elif angka < 20:
        print(f"{angka} Adalah Angka Belasan")

    elif angka < 100:
        print(f"{angka} Adalah Angka Puluhan")

    elif angka < 1000:
        print(f"{angka} Adalah Angka Ratusan")

    elif angka < 100000:
        print(f"{angka} Adalah Angka Ribuan")

    elif angka < 10000000:
        print(f"{angka} Adalah Angka Jutaan")

    elif angka < 1000000000:
        print(f"{angka} Adalah Angka Miliaran")

    elif angka < 100000000000:
        print(f"{angka} Adalah Angka Triliun")

    elif angka < 10000000000000:
        print(f"{angka} Adalah Angka Kuadriliun")

    elif angka < 1000000000000000:
        print(f"{angka} Adalah Angka Kuintiliun")

    elif angka < 100000000000000000:
        print(f"{angka} Adalah Angka Sekstiliun")

    else:
        print("Input Invalid")

bilangan()