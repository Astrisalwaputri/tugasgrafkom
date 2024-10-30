import matplotlib.pyplot as plt
import numpy as np

# Fungsi sederhana untuk menggambar lingkaran
def draw_circle(a, b, r):
    # Sudut lingkaran dari 0 hingga 360 derajat
    theta = np.linspace(0, 2 * np.pi, 100)

    # Hitung titik x dan y berdasarkan sudut
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    # Gambar lingkaran dan titik pusat
    plt.figure(figsize=(8, 6))  # ukuran gambar
    plt.plot(x, y, color='black', label=f'Lingkaran dengan Jari-jari {r}')
    plt.scatter(a, b, color='black')  # Titik pusat

    # Tambahkan teks titik pusat dan jari-jari di luar garis lingkaran
    plt.text(a, b + 0.5, f'Titik Pusat: ({a}, {b})', color='red', ha='center')
    
    # Pengaturan tampilan grafik
    plt.title('Gambar Lingkaran')  # Judul grafik 
    plt.xlabel('SUMBU X')  # Label sumbu X
    plt.ylabel('SUMBU Y')  # Label sumbu Y
    plt.grid(True)  # Tampilkan grid
    plt.axis('equal')  # Pastikan lingkaran tidak terlihat oval

    # Tampilkan legenda tanpa garis
    plt.legend(loc='upper right', handlelength=0, frameon=True)
    plt.show()  # Tampilkan gambar

# Contoh penggunaan
a = 7  # Koordinat x pusat
b = 8  # Koordinat y pusat
r = 4  # Jari-jari lingkaran
draw_circle(a, b, r)  # Panggil fungsi untuk menggambar lingkaran