import os
os.system('cls')
import random
import time

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program  Taruhan Balap siput

print(30*("="))
print("Selamat datang di program balap siput")
print(30*("="))


def siput_resink(siput_balap):
    print("Taruhan siput Resink")
    for idx, siput in enumerate (siput_balap, start=1):
        print(f"{idx}. {siput}")

def get_user_bet(siput_balap): 
    global duit
    global taruhan
    taruhan = int(input("Berani Berapa?? "))
    duit = taruhan * 15
    pilih = int(input("Pilih siput Kepercayaan Mu Dengan Memasukan Nomer siput Resink: "))
    if 1 <= pilih <= len(siput_balap):
        return siput_balap[pilih - 1]
    else:
        print ("KUNEEEEEEEEEEEEEEEMM")
        return get_user_bet(siput_balap)
            
def balap(siput_balap):
    print("\nThe resink is starting!!")
    time.sleep(1)
    balap_progress = {siput: 0 for siput in siput_balap}
    while True:
        for siput in siput_balap:
            balap_progress[siput] += random.randint(1, 10)
            print(f"{siput} DI POSISI {balap_progress[siput]}")
            time.sleep(0.5)

            if balap_progress[siput] >= 100:

                print(f"\n {siput} MENANG BALAP!")
                return siput
            
def main():
    siput_balap = ["AMBATUKAM", "SIPUT HYTAM", "AMBATRON", "APOKADO", "PAGIAN NGAWI", "MUWANI", "DODOT", "RUSDI","MR.IRONI","SI IMUT","AMBAHORSE", "ADIT SLEBEW", "RUSDI SUPER", "SUPERSTAR JUMBO", "PANGERAN NGAWI"]
    siput_resink(siput_balap)

    user_bet = get_user_bet(siput_balap)
    print(f"ANDA MEMILIH: {user_bet}")

    winner = balap(siput_balap)

    if user_bet == winner:
        print("Selamat Anda Menang Taruhan")
        print("Jumlah Uang Yang Anda Menangkan adalah", duit, "RUPIAH")
    else:
        print("YAHHHH TEKOR BOS")
        print("DUIT -", taruhan,"RUPIAH")

if __name__ == "__main__":
    main()