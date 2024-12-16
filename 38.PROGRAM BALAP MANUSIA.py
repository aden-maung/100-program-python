import os
os.system('cls')
import random
import time

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program  Taruhan Balap manusia

print(30*("="))
print("Selamat datang di program balap manusia")
print(30*("="))


def manusia_resink(manusia_balap):
    print("Taruhan manusia Resink")
    for idx, manusia in enumerate (manusia_balap, start=1):
        print(f"{idx}. {manusia}")

def get_user_bet(manusia_balap): 
    global duit
    global taruhan
    taruhan = int(input("Berani Berapa?? "))
    duit = taruhan * 15
    pilih = int(input("Pilih manusia Kepercayaan Mu Dengan Memasukan Nomer manusia Resink: "))
    if 1 <= pilih <= len(manusia_balap):
        return manusia_balap[pilih - 1]
    else:
        print ("KUNEEEEEEEEEEEEEEEMM")
        return get_user_bet(manusia_balap)
            
def balap(manusia_balap):
    print("\nThe resink is starting!!")
    time.sleep(1)
    balap_progress = {manusia: 0 for manusia in manusia_balap}
    while True:
        for manusia in manusia_balap:
            balap_progress[manusia] += random.randint(1, 10)
            print(f"{manusia} DI POSISI {balap_progress[manusia]}")
            time.sleep(0.5)

            if balap_progress[manusia] >= 100:

                print(f"\n {manusia} MENANG BALAP!")
                return manusia
            
def main():
    manusia_balap = ["AMBATUKAM", "ORANG HYTAM", "AMBATRON", "APOKADO", "PAGIAN NGAWI", "MUWANI", "DODOT", "RUSDI","MR.IRONI","SI IMUT","AMBAHORSE", "ADIT SLEBEW", "RUSDI SUPER", "SUPERSTAR JUMBO", "PANGERAN NGAWI"]
    manusia_resink(manusia_balap)

    user_bet = get_user_bet(manusia_balap)
    print(f"ANDA MEMILIH: {user_bet}")

    winner = balap(manusia_balap)

    if user_bet == winner:
        print("Selamat Anda Menang Taruhan")
        print("Jumlah Uang Yang Anda Menangkan adalah", duit, "RUPIAH")
    else:
        print("YAHHHH TEKOR BOS")
        print("DUIT -", taruhan,"RUPIAH")

if __name__ == "__main__":
    main()