#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 4/11/2024
#Ini Adalah Program Menghitung Hari
import os
os.system('cls')

print("-"*40)
print("PROGRAM MENGHITUNG HARI".center(40))
print("-"*40)

HARI_DETIK = 60 * 60 *24
JAM_DETIK = 60 * 60
detik = int(input('Detik: '))
hari = int(detik / HARI_DETIK)
detik = detik % HARI_DETIK
jam = int(detik % HARI_DETIK)
detik = detik % JAM_DETIK
menit =  int(detik / 60)
detik = detik % 60

print(hari, ' hari',jam, ' jam' ,menit, ' menit ', ' dan ',detik,' detik ')
# ... hari ..jam ..menit ..detik