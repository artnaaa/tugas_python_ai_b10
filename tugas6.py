import numpy as np
import pandas as pd
import os

# Set seed agar output random selalu sama setiap kali dijalankan
np.random.seed(42)

# 1. NUMPY - DATA & STATISTIK
# Membuat array nilai ujian (10 data) secara acak antara 50 sampai 100
nilai_ujian = np.random.randint(50, 101, size=10)

# Menghitung Statistik
rata_rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# 2. PANDAS - DATAFRAME 
data_mhs = {
    "nama": ["Arif", "Budi", "Citra", "Dedi", "Eka"],
    "nim": ["A01", "A02", "A03", "A04", "A05"],
    "nilai": nilai_ujian[:5] # Mengambil 5 data pertama dari array NumPy
}

df = pd.DataFrame(data_mhs)

# Menambahkan kolom status
df['status'] = df['nilai'].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# 3. OOP - GRADEBOOK
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Menghitung rata-rata kolom nilai."""
        return self.df['nilai'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase kelulusan."""
        lulus = self.df[self.df['nilai'] >= threshold]
        return (len(lulus) / len(self.df)) * 100

    def save_summary(self, path: str):
        """Menulis ringkasan ke file .txt."""
        jumlah_lulus = len(self.df[self.df['status'] == "LULUS"])
        jumlah_tidak = len(self.df[self.df['status'] == "TIDAK LULUS"])
        
        with open(path, 'w') as f:
            f.write("=== RINGKASAN TUGAS 6 ===\n")
            f.write(f"Rata-rata (NumPy All): {rata_rata}\n")
            f.write(f"Median: {median}\n")
            f.write(f"Standar Deviasi: {std_dev:.2f}\n")
            f.write(f"Min/Max: {nilai_min}/{nilai_max}\n")
            f.write("-" * 25 + "\n")
            f.write(f"Total Mahasiswa di DF: {len(self.df)}\n")
            f.write(f"Jumlah Lulus: {jumlah_lulus}\n")
            f.write(f"Jumlah Tidak Lulus: {jumlah_tidak}\n")
            f.write(f"Persentase Kelulusan: {self.pass_rate()}%")

    def __str__(self) -> str:
        return f"GradeBook(Data={len(self.df)}, Rata-rata={self.average():.2f})"

# 4. DEMO
if __name__ == "__main__":
    # Bagian NumPy
    print("=== NUMPY ===")
    print(f"Nilai Ujian: {nilai_ujian}")
    print(f"Rata-rata: {rata_rata}, Median: {median}, Std Dev: {std_dev:.2f}")

    # Bagian Pandas
    print("\n=== PANDAS ===")
    print(df.head())

    # Bagian OOP
    print("\n=== OOP: GRADEBOOK ===")
    book = GradeBook(df)
    print(book)
    print(f"Average Nilai di DF: {book.average()}")
    print(f"Pass Rate: {book.pass_rate()}%")
    
    # Simpan ke File
    file_path = "ringkasan_tugas6.txt"
    book.save_summary(file_path)
    print(f"\n[INFO] Ringkasan telah disimpan ke {os.path.abspath(file_path)}")