# 📝 Analisis Data Nilai Siswa

Project ini dibuat untuk menganalisis data nilai siswa menggunakan Python.  
Analisis meliputi informasi dataset, statistik deskriptif, ukuran pemusatan data, nilai maksimum & minimum per mapel, serta visualisasi grafik menggunakan matplotlib dan seaborn.

---

## 📂 Struktur Project

Project/
│── nilai_siswa.csv
│── praktikumanalisis.py
│── README.md

---

## 📦 Instalasi Library

Sebelum menjalankan program, install library berikut terlebih dahulu:
python -m pip install pandas
python -m pip install matplotlib
python -m pip install seaborn


---

## ▶️ Cara Menjalankan Program

1. Pastikan file `praktikumanalisis.py` dan `nilai_siswa.csv` berada dalam satu folder.
2. Buka folder tersebut di VS Code.
3. Buka terminal di VS Code.
4. Jalankan program menggunakan perintah:

---

## 📘 Penjelasan Program

### ⭐ 1. Import Library
Program menggunakan beberapa library berikut:
- **pandas** → membaca dan mengelola data CSV  
- **matplotlib** → membuat grafik batang  
- **seaborn** → membuat boxplot  

### ⭐ 2. Membaca Dataset CSV
Program membaca file CSV menggunakan:

```python
data = pd.read_csv('nilai_siswa.csv')

⭐ 3. Informasi Dataset

Program menampilkan:

Total data

Tipe data

Informasi setiap kolom

⭐ 4. Menampilkan 5 Data Pertama

Untuk mengecek struktur awal dataset.

⭐ 5. Statistik Deskriptif

Meliputi:

Rata-rata

Standard deviasi

Minimum

Maximum

Quartile

⭐ 6. Ukuran Pemusatan Data

Program menampilkan:

Mean (Rata-rata)

Median

Modus

⭐ 7. Nilai Maksimum & Minimum Per Mapel

Menggunakan groupby:
data.groupby('Mapel')['Nilai'].agg(['max', 'min'])

⭐ 8. Visualisasi Data

Program menampilkan:
Grafik batang untuk rata-rata nilai per mapel
Boxplot untuk sebaran nilai per mapel

✔️ Kesimpulan

Dari hasil analisis yang dilakukan, dapat dilihat bahwa:

Setiap mata pelajaran memiliki rata-rata nilai yang berbeda-beda.

Nilai maksimum dan minimum tiap mapel dapat diperbandingkan.

Grafik batang dan boxplot membantu memvisualisasikan performa siswa.

Statistik deskriptif memberikan gambaran umum terhadap distribusi data nilai siswa.
