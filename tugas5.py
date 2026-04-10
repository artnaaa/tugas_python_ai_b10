# 1. FUNCTIONS

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """Mengembalikan rata-rata (2 angka di belakang koma)."""
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)


# 2. CLASS

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = [] # Awalnya kosong sesuai instruksi

    def tambah_nilai(self, skor: float):
        """Menambah satu nilai ke list."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Menghitung rata-rata nilai menggunakan function rata_rata di luar class."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Menentukan status kelulusan."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        """Representasi string objek Student."""
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


# 3. DEMO

if __name__ == "__main__":
    # Demo Functions
    print("=== FUNCTIONS ===")
    print(greet("Dunia"))
    print(f"Tambah (5 + 7): {tambah(5, 7)}")
    print(f"Tambah (10 + default): {tambah(10)}")
    print(f"Rata-rata [80, 90, 100]: {rata_rata([80, 90, 100])}")
    print(f"Rata-rata []: {rata_rata([])}")
    
    print("\n=== CLASS STUDENT ===")
    
    # Mahasiswa 1
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(85.0)
    mhs1.tambah_nilai(80.0)
    print(mhs1) # Memanggil __str__
    
    # Mahasiswa 2
    mhs2 = Student("Siti", "B456")
    mhs2.tambah_nilai(60.5)
    mhs2.tambah_nilai(65.0)
    print(mhs2)
    print(f"Detail {mhs2.nama}: Rata-rata = {mhs2.rata_nilai()}, Status = {mhs2.status()}")