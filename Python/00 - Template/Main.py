""" Bab 1
Mari belajar Python Basic """
print("Hello")
print("World!!!")
# Contoh sebagai komen/penanda
a = 10   #disini juga bisa sebagai penanda
Panjang = 1000
"""Contoh komen 
multiline"""
print(a)
print("Nilai Panjang = ", Panjang)

""" Bab 2 
Penamaan """ 
nilai_y = 77
Juta10 = 10000000
"""Jika ada spasi harus ada tanda_
dan penulisan angka harus dibelakang atau terbalik"""
# mari kita spawn 
print("nilai_y = ", nilai_y)
print(Juta10)
# Variabel bisa kita ganti dan dipanggil kembali
nilai_y = 88
print("nilai_y = ", nilai_y)

""" Bab 3
Assignment Indirect """
# asignment indirect ialah merubah variabel
# contoh disini nilai_y kita ubah menjadi b
b = nilai_y
print("b = ", b)

""" Bab 4
Casting """
# Casting yaitu merubah tipe data dari satu tipe ke tipe lain
# Tipe data ada 4, yaitu = integer/int, float, string/str, boolean/bool
# Untuk boolean 1 berarti false, 0 berarti true
data_int = 9;
print("data = ", data_int, ",type =", type(data_int))
# Disini kita mengubah dari integer menjadi float
data_float = float(data_int)
print("data = ", data_float, ",type =", type(data_float))
# Disini kita mengubah dari integer menjadi string
data_str = str(data_int) 
print("data = ", data_str, ",type =", type(data_str))
# Disini kita mengubah dari integer menjadi bool
data_bool = bool(data_int)
print("data = ", data_bool, ",type =", type(data_bool))

""" Bab 5
Input Data """
# Input data yang dimasukan pasti berbentuk string
"""data = input("masukan data: ")
print("data = ",data, ",type =", type(data))
# Disini kita akan mengubah tipe data menjadi integer menggunakan casting
Angka = int(input("masukan angka: "))
print("data = ",Angka, ",type =", type(Angka))
# Sekarang yang lebih kompleks yaitu mengubah ke boolean
# Jadi tekniknya adalah dari data string kita harus mengubah terlebih dahulu ke tipe integer
boolean = bool(int(input("masukan angka: ")))
print("data = ",boolean, ",type =", type(boolean))"""

""" Bab 6
Operasi Aritmatika """
# Penjumlahan = +
# Pengurangan = -
# Perkalian = *
# Perpangkatan = **
# Pembagian = /
# Floor division atau pembagian yang dibulatkan = //
# Modulus atau sisa dari pembagian = %
# Prioritas operasi artimatika dimulai dari kiri dan juga diutamakan perkalian, pembagian
# Prioritas operasi aritmatika bisa dengan ditambahkan tanda ()
# Operasi Aritmatika tidak bisa mencampurkan tipe data yang berbeda
a = 10
b = 3
# Operasi Eksponen / Perpangkatan **
hasil = a ** b
print(a, '**', b, '=', hasil)
# Operasi Pembagian *
hasil = a / b
print(a, '/', b, '=', hasil)
# Operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)
# Operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

""" Bab 7
Latihan Konversi Suhu Celcius ke satuan lainnya """
# Kita akan membuat input untuk suhu celcius
"""print("\nProgram Konversi Temperature\n")
Celcius = float(input("Masukan suhu dalam Celcius: "))
print("Suhu adalah", Celcius, "Celcius")
# Reamur
Reamur = (4/5) * Celcius
print("Suhu adalah", Reamur, "Reamur")
# Fahrenheit
Fahrenheit = ((9/5) * Celcius) + 32
print("Suhu adalah", Fahrenheit, "Fahrenheit")
#Kelvin
Kelvin = Celcius + 273
print("Suhu adalah", Kelvin, "Kelvin")"""

""" Bab 8
Operasi Komparasi """
# Lebih dari : >
# Lebih dari sama dengan : >=
# Kurang dari : <
# Kurang dari sama dengan : <=
# Sama dengan : ==
# Tidak sama dengan !=
# Betul = is
# salah = is not
a = 2
b = 2
# Contoh Lebih dari
hasil = a > b
print(a, ">", b, "=", hasil)
# Contoh Kurang dari sama dengan
hasil = a <= b
print(a, "<=", b, "=", hasil)
# Contoh Tidak sama dengan 
hasil = a != b
print(a, "!=", b, "=", hasil)
# Contoh is dan is not
c = 4
d = 4
hasil = c is d
print("c is d =", hasil)
hasil = c is not d
print("c is not d =", hasil)

""" Bab 9
Operasi Logika atau Tabel Kebenaran """
# Operasi Logika ada 4 : not, or, and, xor(^)

print('--------NOT--------')
A = True
B = not A
print('Data A =', A)
print('Data B =', B)
# Kesimpulannya not adalah kebalikan

print("--------OR--------")
A = True
B = False
C = A or B
print(A, 'or', B, '=', C)
A = False
B = True
C = A or B
print(A, 'or', B, '=', C)
A = True
B = True
C = A or B
print(A, 'or', B, '=', C)
A = False
B = False
C = A or B
print(A, 'or', B, '=', C)
# Kesimpulan or adalah jika salah satu true maka hasilnya true 
# atau seperti penjumlahan dengan 0 = false dan 1 = true

print("--------AND--------")
A = True
B = False
C = A and B
print(A, 'and', B, '=', C)
A = False
B = True
C = A and B
print(A, 'and', B, '=', C)
A = True
B = True
C = A and B
print(A, 'and', B, '=', C)
A = False
B = False
C = A and B
print(A, 'and', B, '=', C)
# Kesimpulan and adalah jika salah satu false maka hasilnya akan false
# atau seperti Perkalian dengan 0 = false dan 1 = true

print("--------XOR--------")
A = True
B = False
C = A ^ B
print(A, 'xor', B, '=', C)
A = False
B = True
C = A ^ B
print(A, 'xor', B, '=', C)
A = True
B = True
C = A ^ B
print(A, 'xor', B, '=', C)
A = False
B = False
C = A ^ B
print(A, 'xor', B, '=', C)
# Kesimpulan xor adalah Akan true jika salah satu ada true tetapi jika ada dua true dia akan false
# atau akan true jika berbeda dan akan false jika sama

""" Bab 10
Operasi Logika dan Komparasi, Irisan dan Gabungan"""
# Kita akan membuat irisan atau gabungan seperti di matematika
# Daerah + berarti termasuk dalam himpunan penyelesaian

# Contoh Kasus Gabungan, Keywordnya "or"
# ++++++3------10++++++ 
inputuser = float(input("Masukan Angka\nKurang dari 3\nLebih dari 10\n:"))
# ++++++3------
IsKurangDari3 = (inputuser < 3)
print("Kurang dari 3 =", IsKurangDari3)
# ------10++++++
IsLebihDari10 = (inputuser > 10)
print("Lebih dari 10 =", IsLebihDari10 )
# Sekarang kita gabungkan dengan metode or
IsCorrect = (IsKurangDari3 or IsLebihDari10)
print("Angka yang Dimasukan :", IsCorrect)

print("\n", 10*"=", "\n")

# Contoh Kasus Irisan, Keywordnya "and"
# ------3++++++10------
inputuser2 = float(input("Masukan Angka\nLebih dari 3\nKurang Dari 10\n:"))
# ------3++++++
IsLebihDari3 = (inputuser2 > 3)
print("Lebih dari 3 =", IsLebihDari3)
# ++++++10------
IsKurangDari10 = (inputuser2 < 10)
print("Kurang dari 10 =", IsKurangDari10)
IsCorrect2 = (IsLebihDari3 and IsKurangDari10)
print("Angka yang Dimasukan =", IsCorrect2)

""" Bab 11
Operator Assignment """
# Operator Assignment adalah penyingkatan, jadi operasi yang akan dilakukan diringkas

# Contoh Operasi Aritmatika Ringkas
Z = 10
print("Nilai Z =", 10)
Z *= 2
print("Nilai Z * 2 =", Z)

# Contoh Operasi Bitwise Ringkas
Y = False
print("Y =", Y)
Y |= True
print("Hasil False or False atau disingkat, Y |= False adalah", Y)

"""" Bab 12
Operator Bitwise """
# Operator Bitwise adalah operasi yang dilakukan terhadap bit/binary digit

# Contoh cara menampilkan bit seperti di bawah
a = 9
b = 5
print('Nilai a =', a, 'binary :', format(a,'08b'))
print('Nilai b =', b, 'binary :', format(b, '08b'))

# kita akan membuat operator bitwise or |
c = a | b
print('Nilai a | b =', c, 'binary :', format(c, '08b'))

# kita akan membuat operator bitwise and &
c = a & b
print('Nilai a & b =', c, 'binary :', format(c, '08b'))

# Kita akan membuat operator bitwise xor ^
c = a ^ b
print('Nilai a ^ b =', c, 'binary :', format(c, '08b'))

# Kita akan membuat opertor bitwise not ~
c = ~a
print('Nilai ~a =', c, 'binary :', format(c, '08b'))

# Shifting yaitu menggeser binary digit
#Shifting right >>
c = a >> 2
print('Nilai a >> 2 =', c, 'binary :', format(c, '08b'))

# Shifting left <<
c = a << 1
print('Nilai a << 1 =', c, 'binary :', format(c, '08b'))

""" Bab 13
Pengenalan String, dan Tata Bahasa """
# Cara Membuat String
'''
    String menggunakan Single Quote '...'
    String menggunakan Double Quote "..."
'''
# 1. Membuat tanda ' menjadi string
# Sekarang hari jum'at, Pakat tanda \ sebelum ' agar terbaca string
print('Sekarang hari jum\'at') 

# 2. Backslash \, Jika ada backslash yang ingin dijadikan string, harus di double
print('C:\\user\\Ivan')

# 3. tab \t atau membuat spasi lebih jauh
print('a\tdan\tb berjauhan')

# Backspace \b atau mendekatkan string
print('a \bb berdekatan')

# New line(enter) \n \r \r\n
# CR/Carriage Return ~> Biasa digunakan di MacOS, Linux. Unix
print('Baris Pertama \rBaris Kedua')
# LF/Line Feed ~> Biasa digunakan di Commodore, Acorn, Lisp
print('Baris Pertama \nBaris Kedua')
# CRLF/Carriage Return Line Feed ~> Biasa digunakan di Windows
print('Baris Pertama \r\nBaris Kedua')

# Raw String / r, Untuk mengubah string menjadi raw dan bebas untuk di custom
print(r'C:/new folder')

# Multiline Literal String, Fungsinya sama seperti New Line
print("""Baris Kesatu
Baris Kedua""")

""" Bab Tambahan
If else """
# Ini adalah contoh if else python
spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)



