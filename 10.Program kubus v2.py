#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program kubus V2
print("="*40)
print("PROGRAM KUBUS".center(40))
print("="*40)

r = float(input("masukan jari jari: "))
pi = 3.14
l = lambda pi: pi * r**2
k = lambda pi,r:2 * pi * r

print(f"luas = {l(pi)} cm2")
print(f"keliling = {k(pi,r)} cm")