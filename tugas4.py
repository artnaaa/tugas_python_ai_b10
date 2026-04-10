# 1. List - akses & manipulasi
buah_favorit = ["jambu", "nanas", "alpukat", "mangga", "jeruk"]
print(f"List Awal: {buah_favorit}")

# Akses & Slicing
print (f"Pertama: {buah_favorit[0]}, Terakhir: {buah_favorit[-1]}")
print(f"Slicing [1:5:2]: {buah_favorit[1:5:2]}")

# Manipulasi
buah_favorit.append("pisang") # Menambahkan elemen baru
buah_favorit.insert(2, "semangka") # Menyisipkan elemen di indeks 2
buah_favorit.extend(["melon", "kiwi"]) # Menambahkan beberapa elemen sekaligus
buah_favorit.pop(3) # Menghapus elemen di indeks 3

print(f"List Setelah Manipulasi: {buah_favorit}")


# 2. Tuple – immutability & unpacking

# Tuple
my_tuple = ("Mentor", "Peserta", "Modul", "Tugas", "Lulus")
print(f"Panjang Tuple: {len(my_tuple)}")
print(f"Elemen Index 2: {my_tuple[2]}")

# Unpacking
posisi1, posisi2, *sisanya = my_tuple
print(f"Unpacked: {posisi1}, {posisi2}, Sisanya: {sisanya}")


# 3. Set – keunikan & operasi himpunan
set_a = {1, 2, 3, 4, 5, 5, 5} # Coba masukkan duplikat
set_b = {4, 5, 6, 7, 8}

print(f"Set A (Duplikat hilang): {set_a}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A-B): {set_a - set_b}")
print(f"Symmetric Difference: {set_a ^ set_b}")


# 4. Dictionary – key-value dasar
mhs = {"nama": "Aruna", "nim": "A123", "angkatan": 2024, "kota": "Jakarta"}

# Operasi
mhs["prodi"] = "Informatika" # Tambah key
mhs["kota"] = "Batam"        # Ubah nilai
del mhs["angkatan"]          # Hapus key

print(f"Keys: {list(mhs.keys())}")
print(f"Values: {list(mhs.values())}")
print(f"Items: {list(mhs.items())}")

# Iterasi
for k, v in mhs.items():
    print(f"{k}: {v}")


# 5. Nested structures
perpustakaan = [
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018},
    {"judul": "Clean Code", "penulis": "Robert Martin", "tahun": 2008},
    {"judul": "Python Crash Course", "penulis": "Eric Matthes", "tahun": 2019},
    {"judul": "The Hobbit", "penulis": "Tolkien", "tahun": 1937}
]

# Loop cetak judul
print("Daftar Judul:")
for buku in perpustakaan:
    print(f"- {buku['judul']}")

# Filter buku >= 2010 (List Comprehension)
buku_baru = [b['judul'] for b in perpustakaan if b['tahun'] >= 2010]
print(f"Buku Terbit >= 2010: {buku_baru}")


# 6. Comprehension & utilitas
# List Comprehension
genap = [x for x in range(1, 21) if x % 2 == 0]
kuadrat = [x**2 for x in range(1, 21)]

# Dict Comprehension
status_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}

# Set Comprehension
kalimat = "Infinite Learning Batch Sepuluh"
huruf_unik = {char.lower() for char in kalimat if char.isalpha()}

print(f"Angka Genap: {genap}")
print(f"Huruf Unik: {huruf_unik}")


# 7. Keanggotaan && pencarian sederhana
buah = ["apel", "jeruk", "mangga"]

# Cek Keanggotaan
cari = "jeruk"
if cari in buah:
    print(f"{cari} ditemukan pada posisi index {buah.index(cari)}")
else:
    print(f"{cari} tidak ada dalam daftar")

# Cek pada Set (Sangat cepat untuk data besar)
warna = {"merah", "hijau"}
print("Apakah 'biru' ada di set warna?", "biru" in warna)
