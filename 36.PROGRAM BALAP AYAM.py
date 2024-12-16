import os
os.system('cls')
import random
import time

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program  Taruhan Balap ayam

print(30*("="))
print("Selamat datang di program balap ayam")
print(30*("="))


def ayam_resink(ayam_balap):
    print("Taruhan ayam Resink")
    for idx, ayam in enumerate (ayam_balap, start=1):
        print(f"{idx}. {ayam}")

def get_user_bet(ayam_balap): 
    global duit
    global taruhan
    taruhan = int(input("Berani Berapa?? "))
    duit = taruhan * 15
    pilih = int(input("Pilih ayam Kepercayaan Mu Dengan Memasukan Nomer ayam Resink: "))
    if 1 <= pilih <= len(ayam_balap):
        return ayam_balap[pilih - 1]
    else:
        print ("KUNEEEEEEEEEEEEEEEMM")
        return get_user_bet(ayam_balap)
            
def balap(ayam_balap):
    print("\nThe resink is starting!!")
    time.sleep(1)
    balap_progress = {ayam: 0 for ayam in ayam_balap}
    while True:
        for ayam in ayam_balap:
            balap_progress[ayam] += random.randint(1, 10)
            print(f"{ayam} DI POSISI {balap_progress[ayam]}")
            time.sleep(0.5)

            if balap_progress[ayam] >= 100:

                print(f"\n {ayam} MENANG BALAP!")
                return ayam
            
def main():
    ayam_balap = ["AMBATUKAM", "AYAM HYTAM", "AMBATRON", "APOKADO", "PAGIAN NGAWI", "MUWANI", "DODOT", "RUSDI","MR.IRONI","SI IMUT","AMBAHORSE", "ADIT SLEBEW", "RUSDI SUPER", "SUPERSTAR JUMBO", "PANGERAN NGAWI"]
    ayam_resink(ayam_balap)

    user_bet = get_user_bet(ayam_balap)
    print(f"ANDA MEMILIH: {user_bet}")

    winner = balap(ayam_balap)

    if user_bet == winner:
        print("Selamat Anda Menang Taruhan")
        print("Jumlah Uang Yang Anda Menangkan adalah", duit, "RUPIAH")
    else:
        print("YAHHHH TEKOR BOS")
        print("DUIT -", taruhan,"RUPIAH")

if __name__ == "__main__":
    main()