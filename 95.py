import os
os.system('cls')

# Di buat oleh Rashqa Andrean Fitrah Sulaeman
# Di Buat Tanggal 18/11/2024
# Ini Adalah Program Pengurutan Angka dengan Metode Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Menemukan titik tengah
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)   # Memanggil merge_sort pada sisi kiri
        merge_sort(right)  # Memanggil merge_sort pada sisi kanan

        i = j = k = 0

        # Menggabungkan dua sisi yang sudah diurutkan
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Memastikan jika ada elemen yang tersisa
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def main():
    angka = list(map(int, input("Masukkan angka yang akan diurutkan (pisahkan dengan spasi): ").split()))
    print("Angka sebelum diurutkan:", angka)
    angka_terurut = merge_sort(angka)
    print("Angka setelah diurutkan:", angka_terurut)

main()
