import os
os.system('cls')

#Di buat oleh Rashqa Andrean Fitrah Sulaeman
#Di Buat Tanggal 18/11/2024
#Ini Adalah Program simple kalkulator

def main():
    angka1 = float(input("Masukan angka pertama: ")) 
    angka2 = float(input("Masukan angka kedua: ")) 
    operasi = str(input("Pilih Perhitungan: +, -, x, /: "))

    if operasi == '+':
        hasil = angka1 + angka2
    elif operasi == '-':
        hasil = angka1 - angka2
    elif operasi == 'x':
        hasil = angka1 * angka2
    elif operasi == '/':
        if angka1 or angka2 == 0:
            print("Tidak bisa di bagi dengan 0")
        else:
            hasil = angka1 / angka2
    else:
        print("Input invalid")
    print(f"Hasilnya adalah {hasil}")

    return hasil

main()
    
            
        

    
    


