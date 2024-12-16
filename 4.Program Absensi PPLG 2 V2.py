#Program ini dibuat tanggal 6/11/2024
#Rashqa Andrean Fitrah Sulaeman
#Program Absensi Siswa Kelas X PPLG 2
import os
os.system('cls')

# dictionary nomer absen kelas x pplg 2

students = {
    1: ("Adiftya Rahman", "Laki-Laki", "X PPLG 2", "0896-4814-3878"),
    2: ("Alyandra Aditya", "Laki-Laki", "X PPLG 2", "0896-8219-5300"),
    3: ("Andhika Noor Hidayat", "Laki-Laki", "X PPLG 2", "0821-1706-9415"),
    4: ("Bama Maulana Wibisana", "Laki-Laki", "X PPLG 2", "0857-2315-1325"),
    5: ("Dika Prayoga Gunawan", "Laki-Laki", "X PPLG 2", "0859-0031-5216"),
    6: ("Dimitar Bayangka Gunawan", "Laki-Laki", "X PPLG 2", "0813-1266-0848"),
    7: ("Dzaky Fadhilah Rahmawan", "Laki-Laki", "X PPLG 2", "0857-2357-9042"),
    8: ("Fariz Dzulhami", "Laki-Laki", "X PPLG 2", "0878-6073-0473"),
    9: ("Ibnu Hambal Al Bantani RCH", "Laki-Laki", "X PPLG 2", "0878-4872-8427"),
    10: ("Ilisha Neola Pino", "Perempuan", "X PPLG 2", "0812-9633-4992"),
    11: ("Jibril Ibni Jubair", "Laki-Laki", "X PPLG 2", "0857-8002-7462"),
    12: ("Jihan Fauziah", "Perempuan", "X PPLG 2", "0895-6269-50607"),
    13: ("Kiano Devaro Ridho", "Laki-Laki", "X PPLG 2", "0895-2808-0314"),
    14: ("M Arkan Raihan Nugraha", "Laki-Laki", "X PPLG 2", "0814-6225-6193"),
    15: ("M Raffi Nadhir Abdurrahman", "Laki-Laki", "X PPLG 2", "0852-2078-3332"),
    16: ("M Afdal Firmansyah", "Laki-Laki", "X PPLG 2", "0877-3128-7270"),
    17: ("M Fajar Maulana", "Laki-Laki", "X PPLG 2", "0838-7866-1359"),
    18: ("M Arsa Prayata", "Laki-Laki", "X PPLG 2", "0857-0309-1434"),
    19: ("M Asyraf Rizqullah", "Laki-Laki", "X PPLG 2", "0877-6713-8388"),
    20: ("M Haidar Almer Rafif", "Laki-Laki", "X PPLG 2", "0859-5626-7079"),
    21: ("M Rofi'i Al Awi", "Laki-Laki", "X PPLG 2", "0878-1282-2400"),
    22: ("Nazwatus Syfa", "Perempuan", "X PPLG 2", "0878-1847-5075"),
    23: ("Nesya Kirrani Nurrofi", "Perempuan", "X PPLG 2", "0878-2008-6222"),
    24: ("Panca Satya Nugraha", "Laki-Laki", "X PPLG 2", "0822-1888-7613"),
    25: ("Putri Maulida Yusuf", "Perempuan", "X PPLG 2", "0831-8639-5470"),
    26: ("Rahma Santtika Al Anshori", "Perempuan", "X PPLG 2", "0878-1600-6288"),
    27: ("Resna Rahmawati", "Perempuan", "X PPLG 2", "0812-1224-0358"),
    28: ("Revan Kautsar Mulyana", "Laki-Laki", "X PPLG 2", "0895-3604-87763"),
    29: ("Syahira Bilqis Nuhaira", "Perempuan", "X PPLG 2", "0857-3339-8113"),
    30: ("Rafa Khadafi", "Laki-Laki", "X PPLG 2", "0857-6789-9904"),
    31: ("Rheivan Zahran Abinaya", "Laki-Laki", "X PPLG 2", "0874-2738-2727"),
    32: ("Rashqa Andrean Fitrah Sulaeman", "Laki-Laki", "X PPLG 2", "0857-2389-4370"),
    33: ("Resna Rahmawati", "Perempuan", "X PPLG 2", "0812-1224-0358"),
    34: ("Revan Kautsar Mulyana", "Laki-Laki","X PPLG 2", "0895-3604-87763"),
    35: ("Rheivan Zahran Abinaya", "Laki-Laki", "X PPLG 2", "0895-3604-87763"),
    36: ("Syahira Bilqis Nuhaira", "Perempuan", "X PPLG 2", "0857-3339-8113")
}

gg = int(input("Masukan No Absen:"))

if gg in students:

    name, gender, kelas, phone = students[gg]
    print("="*60)
    print(f"Nama: {name}")
    print(f"Gender: {gender}")
    print(f"Kelas: {kelas}")
    print(f"No Hp: {phone}")
    print("="*60)
else:
    print("Nomer ini tidak ada dalam absensi kelas X pplg 2\n")
