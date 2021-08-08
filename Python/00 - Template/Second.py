""" Mulai Coding """
# Basic dan Fundamental Coding
Nama = "Ivan"
Jurusan = "Sistem Informasi"
print(Nama + " " + Jurusan)
print("Hi, nama saya " + Nama + ", saya dari jurusan " + Jurusan)
# Penjumlahan = +
# Pengurangan = -
# Perkalian = *
# Pembagian = /
# perhitungan tidak bisa mencampurkan antara tipe data yang berbeda
# muteable = variabel bisa diubah, immutable = tidak bisa diuba; pakai sesuai kebutuhan
# contoh operasi perkalian dan pembagian
a = 69
b = 31
c = a * b
print(c)
a = 77
b = 39
print(a * b / c)

# contoh yang lebih kompleks membuat rumus luas lingkaran yaitu pi x diameter
pi:float = 3.14
diameter:float = 5
print(pi * diameter)

list_values = [1, 2, 3] # ini muteable menggunakan []
set_values = (1, 2, 3) # ini immutable menggunakan ()
list_values[0] = 100 # bagian muteable bisa diubah seperti ini
print(list_values[0])
print(set_values[0])

sudahmakan:bool = True
float = 98
print("data = 98", float, ",type =", type(float))
