# Sistem Antrian SPBU Menggunakan Queue Array

## Judul Program
**Program Sistem Antrian SPBU Menggunakan Queue Array**

## Deskripsi Singkat

Program ini dibuat untuk mengelola antrian kendaraan pada SPBU menggunakan struktur data **Queue Array**. User dapat menambahkan kendaraan ke dalam antrian, memproses kendaraan yang selesai mengisi BBM, melihat kendaraan paling depan, dan menampilkan seluruh antrian kendaraan.

Metode queue yang digunakan menerapkan konsep FIFO (First In First Out), yaitu kendaraan yang pertama masuk akan menjadi kendaraan pertama yang dilayani. Program juga menggunakan konsep **Circular Queue** agar penggunaan array menjadi lebih efisien serta menerapkan exception handling untuk menangani input yang tidak valid.


## Source Code
<img width="1418" height="3788" alt="source code TA4" src="https://github.com/user-attachments/assets/7ccc3b28-5afc-4723-a33e-17f882b3d0ff" />

## Penjelasan Source Code
class QueueArray:  
Membuat class QueueArray untuk mengelola antrian kendaraan menggunakan array.


def __init__(self, max_size=100):  
Fungsi untuk inisialisasi queue. max_size=100 berarti kapasitas maksimal antrian default adalah 100 kendaraan.  
  

self.MAXN = max_size  
Menyimpan kapasitas maksimal antrian ke variabel MAXN.  


self.q = [None] * self.MAXN  
Membuat list/array kosong sebanyak ukuran MAXN.
Semua isi awalnya None.

self.front_idx = -1  
Penanda posisi depan antrian.
-1 berarti antrian masih kosong.  

self.rear_idx = -1  
Penanda posisi belakang antrian.
-1 juga berarti belum ada data.  
  

def is_empty(self):     
Digunakan untuk mengecek apakah antrian kosong.

return self.front_idx == -1    
Jika front_idx bernilai -1, maka queue kosong.


def is_full(self):  
Digunakan untuk mengecek apakah queue penuh.


return (self.rear_idx + 1) % self.MAXN == self.front_idx  
Menggunakan konsep circular queue untuk menentukan kondisi penuh.


def enqueue(self, kendaraan):  
Digunakan untuk menambahkan kendaraan ke dalam antrian.


if self.is_full():   
Mengecek apakah antrian penuh.


print("Antrian SPBU penuh")   
Menampilkan pesan jika queue penuh.


if self.is_empty():  
Mengecek apakah antrian kosong.  

self.front_idx = 0  
Jika kosong, posisi depan diisi indeks 0.  

self.rear_idx = 0  
Posisi belakang juga di indeks 0 karena baru ada 1 kendaraan.  

else:  
Jika antrian tidak kosong.  

self.rear_idx = (self.rear_idx + 1) % self.MAXN  
Geser posisi belakang satu langkah.
Menggunakan % agar bisa melingkar kembali ke awal array.  

self.q[self.rear_idx] = kendaraan   
Menyimpan data kendaraan ke array pada posisi belakang.

print(f"Kendaraan {kendaraan} masuk Antrian")  
Menampilkan pesan kendaraan berhasil masuk antrian.

def dequeue(self):  
Digunakan untuk memproses kendaraan paling depan.


if self.is_empty():  
Mengecek apakah queue kosong.


print("Antrian SPBU kosong")  
Menampilkan pesan jika queue kosong.

return  
Mengembalikan fungsi.

print(f"Kendaraan {self.q[self.front_idx]} selesai mengisi BBM")  
Menampilkan kendaraan yang selesai mengisi BBM.

 
if self.front_idx == self.rear_idx:  
Mengecek apakah queue hanya memiliki satu data.

self.front_idx = -1  
Mengosongkan posisi depan.

self.rear_idx = -1  
Mengosongkan posisi belakang. Artinya antrian kembali kosong.

else:  
Jika masih ada kendaraan lain.

self.front_idx = (self.front_idx + 1) % self.MAXN  
Posisi depan maju satu langkah.

 
def peek(self):  
Digunakan untuk melihat kendaraan paling depan tanpa menghapus data.

if self.is_empty():  
Cek apakah kosong.

print("Antrian SPBU kosong")  
Pesan jika kosong.

return  
Menghentikan fungsi.

print(f"Kendaraan paling depan: {self.q[self.front_idx]}")  
Menampilkan kendaraan paling depan.
 
def display(self):  
Digunakan untuk menampilkan seluruh antrian kendaraan.


if self.is_empty():  
Cek apakah kosong.

print("Antrian SPBU kosong")  
Pesan jika kosong.

return  
Menghentikan fungsi.

print("\nDaftar Antrian kendaraan:")  
Menampilkan judul daftar antrian.

i = self.front_idx  
Variabel i mulai dari posisi depan.

while True:  
Perulangan tanpa batas untuk menampilkan data.

print("-", self.q[i])  
Menampilkan kendaraan pada indeks i.

if i == self.rear_idx:  
Jika sudah sampai posisi belakang.

break  
Menghentikan perulangan.

i = (i + 1) % self.MAXN  
Pindah ke indeks berikutnya secara melingkar.

 
def main():  
Fungsi utama program.

 
SPBU = QueueArray()  
Membuat objek queue bernama `SPBU`.

pilih = 0  
Variabel untuk menyimpan pilihan menu.

while pilih != 5:  
Perulangan menu program sampai user memilih keluar.

print("\n=== SISTEM ANTRIAN SPBU ===")  
Menampilkan judul menu.

print("1. Kendaraan Masuk")  
Menu tambah kendaraan.

print("2. Kendaraan Selesai")  
Menu hapus kendaraan.

print("3. Lihat Antrian Depan")  
Menu melihat kendaraan depan.

print("4. Tampilkan Semua Antrian")  
Menu tampilkan seluruh antrian.

print("5. Keluar")  
Menu keluar program.

try:  
Digunakan untuk menangani error input.

pilih = int(input("Pilih menu: "))  
Meminta user memasukkan pilihan menu.

 
except ValueError:  
Menangkap error jika input bukan angka.

print("Input harus angka!")  
Menampilkan pesan error jika input tidak valid.

continue  
Kembali ke awal perulangan menu.
 

if pilih == 1:  
Jika memilih menu 1.

kendaraan = input("Masukkan nama/plat kendaraan: ")     
Input nama atau plat kendaraan.

SPBU.enqueue(kendaraan)  
Menambahkan kendaraan ke antrian.

elif pilih == 2:  
Jika memilih menu 2.

SPBU.dequeue()  
Menghapus kendaraan depan.

elif pilih == 3:  
Jika memilih menu 3.

SPBU.peek()  
Melihat kendaraan paling depan.

elif pilih == 4:  
Jika memilih menu 4.

SPBU.display()  
Menampilkan seluruh antrian.

elif pilih == 5:  
Jika memilih menu keluar.

print("Program selesai")  
Pesan program selesai.

else:  
Jika menu tidak tersedia.

print("Menu tidak valid")  
Pesan error pilihan menu.

if __name__ == "__main__":  
Mengecek apakah file dijalankan langsung.
 
main()  
Menjalankan fungsi utama program.



## Output Program



## Penjelasan Output



## Link Video Presentasi YouTube

