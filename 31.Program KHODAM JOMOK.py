import os
os.system('cls')
import random

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program Cek Homo

print(60*"=")
print("PROGRAM CEK KHODAM JOMOK".center(60))
print(60*"=")

print("Selamat Datang Di Program Cek KHODAM JOMOK")

def cek_jomok(hasil):
    jomok = {
        1:(" Mas RUSDI "),
        2:(" Mas AMBA "),
        3:(" SI IMUT "),
        4:(" SUPERSTAR JUMBO! "),
        5:(" MS.IRONI "),
        6:(" RUSDI SUPERSTAR "),
        7:(" AMBATRON "),
        8:(" AMBALABU "),
        9:(" PUDING COKLAT MAS AMBALI "),
        10:(" SUSU KENTAL MANIS "),
        11:(" MUANI "),
        12:(" POPMIE "),
        13:(" MAS ADIT "),
        14:(" KEWER KEWER "),
        15:(" KUMALALA "),
        16:(" SAVESTA "),
        17:(" P DIDDY "),
        18:(" AMBASIGMA "),
        19:(" MIKO KAWAII "),
        20:(" CI LILNAS "),
        21:(" FUAD BIN ABDUL ZEUS "),
        22:(" REHAN WANGSAFF "),
        23:(" MAS FAIZ "),
        24:(" DARMAJI "),
        25:(" ANDRE ONANI "),
        26:(" ALL MEMBER JMK48 "),
        27:(" MAS FUAD "),
        28:(" LIL NUS NUS "),
        29:(" MAS NARJI "),
        30:(" KAPAL KARAM "),
    }
    for line in jomok[hasil]:
        print(line)

def kejomokan():
    hasil = random.randint(1,30)
    input("Cek Jomok Sesuai Nama: ")
    cek_jomok(hasil)

kejomokan()

