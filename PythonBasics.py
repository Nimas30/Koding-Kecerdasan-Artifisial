a=3
print(type(a))
print("hello python")

#data float
b=4,5
print(type(b))
#data str
nama="sinta"
print(type(nama))
#data list
angka=[1,2,3,4,5]
print(type(angka))
angka.append(7)
print(angka)

# 1. Variabel dan Tipe Data
int_var = 10
float_var = 3.14
str_var = "Hello"
list_var = [1, 2, 3]

print("Tipe data int_var:", type(int_var))
print("Tipe data float_var:", type(float_var))
print("Tipe data str_var:", type(str_var))
print("Tipe data list_var:", type(list_var))

print("="*40)

# 2. List dan Manipulasi
belanja = ["beras", "minyak", "telur"]

# Tambahkan gula dan kopi
belanja.append("gula")
belanja.append("kopi")

# Tampilkan semua item dengan perulangan
print("Daftar Belanja:")
for item in belanja:
    print("-", item)

print("="*40)

# 3. Dictionary
harga_belanja = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

# Hitung total harga
total = sum(harga_belanja.values())

print("Daftar Harga Belanja:")
for barang, harga in harga_belanja.items():
    print(f"{barang} : Rp{harga}")

print("Total harga belanja:", total)

print("="*40)

# 4. Fungsi
import math

def luas_keliling_lingkaran(r):
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    return luas, keliling

# Contoh penggunaan
r = 7
luas, keliling = luas_keliling_lingkaran(r)
print(f"Luas lingkaran (r={r}) = {luas:.2f}")
print(f"Keliling lingkaran (r={r}) = {keliling:.2f}")

print("="*40)

# 5. Percabangan
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")