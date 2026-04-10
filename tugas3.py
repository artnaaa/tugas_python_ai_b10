# 1. Deklarasi Variabel dan Tipe Data
nama_program = "Infinite Learning"
bergerak_di_bidang = "Edutech"
jumlah_peserta = 8000
skor_akhir = 95.5
is_lulus = True
tech_stack_belajar = ["Python", "Data Science", "AI Models"]


# 2. Manipulasi String
print (nama_program + " " + bergerak_di_bidang)
print (len (nama_program))
print (nama_program.upper())
print (nama_program.lower())


# 3. Operasi Matematika Sederhana
bonus_nilai = 5
total_skor = skor_akhir + bonus_nilai
selisih_peserta = jumlah_peserta - 1000
target_peserta_depan = jumlah_peserta * 2
rata_rata_skor = skor_akhir / 2
pembagian_bulat = 10 // 3 # Hasilnya: 3
sisa_bagi = 10 % 3        # Hasilnya: 1

print(f"Total Skor: {total_skor}")
print(f"Sisa Bagi 10/3: {sisa_bagi}")


# 4. List dan Akses Elemen
mentor_list = ["Mentor A", "Mentor B", "Mentor C", "Mentor D"]
print("Mentor Pertama:", mentor_list[0])  # Output: Mentor A
mentor_list.append("Mentor E")  # Menambahkan mentor baru
print("Daftar Mentor Setelah Penambahan:", mentor_list)
mentor_list.remove("Mentor B")  # Menghapus mentor
print("Daftar Mentor Setelah Penghapusan:", mentor_list)
remove_item = mentor_list.pop(1)  # Menghapus mentor berdasarkan indeks ke 1

print("List Akhir:", mentor_list)
print("Yang di pop:", remove_item)


# 5. Penggunaan Input dari User
nama_user = input ("Masukkan nama Anda: ")
umur_user = int(input ("Masukkan umur Anda: "))
print(f"Selamat datang, {nama_user}! Umur Anda adalah {umur_user}")