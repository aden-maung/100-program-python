import os
os.system('cls')
import random
import time

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program  Taruhan Balap hewan

print(30*("="))
print("Selamat datang di program balap hewan")
print(30*("="))


def hewan_resink(hewan_balap):
    print("Taruhan hewan Resink")
    for idx, hewan in enumerate (hewan_balap, start=1):
        print(f"{idx}. {hewan}")

def get_user_bet(hewan_balap): 
    global duit
    global taruhan
    taruhan = int(input("Berani Berapa?? "))
    duit = taruhan * 15
    pilih = int(input("Pilih hewan Kepercayaan Mu Dengan Memasukan Nomer hewan Resink: "))
    if 1 <= pilih <= len(hewan_balap):
        return hewan_balap[pilih - 1]
    else:
        print ("KUNEEEEEEEEEEEEEEEMM")
        return get_user_bet(hewan_balap)
            
def balap(hewan_balap):
    print("\nThe resink is starting!!")
    time.sleep(1)
    balap_progress = {hewan: 0 for hewan in hewan_balap}
    while True:
        for hewan in hewan_balap:
            balap_progress[hewan] += random.randint(1, 10)
            print(f"{hewan} DI POSISI {balap_progress[hewan]}")
            time.sleep(0.5)

            if balap_progress[hewan] >= 100:

                print(f"\n {hewan} MENANG BALAP!")
                return hewan
            
def main():
    hewan_balap = ["AYAM NEGRO", "CUMI HYTAM", "SAPI", "KELINCI", "KURA-KURA", "CHETAH", "BUAYA", "DINOSAURUS","KUCING","SIPUT","AMBAHORSE", "FARIZ", "RUSDI SUPER", "SUPERSTAR JUMBO", "PANGERAN NGAWI"]
    hewan_resink(hewan_balap)

    user_bet = get_user_bet(hewan_balap)
    print(f"ANDA MEMILIH: {user_bet}")

    winner = balap(hewan_balap)

    if user_bet == winner:
        print("Selamat Anda Menang Taruhan")
        print("Jumlah Uang Yang Anda Menangkan adalah", duit, "RUPIAH")
    else:
        print("YAHHHH TEKOR BOS")
        print("DUIT -", taruhan,"RUPIAH")

if __name__ == "__main__":
    main()