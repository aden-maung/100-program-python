import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Pencarian dengan Algoritma Binary Search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    arr = list(map(int, input("Masukkan angka yang terurut (pisahkan dengan spasi): ").split()))
    x = int(input("Masukkan angka yang ingin dicari: "))
    result = binary_search(arr, x)
    
    if result != -1:
        print(f"Angka ditemukan pada indeks: {result}")
    else:
        print("Angka tidak ditemukan")

main()
