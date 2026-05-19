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
<img width="439" height="859" alt="image" src="https://github.com/user-attachments/assets/91383a0a-d4a8-4969-b5d3-e49115f3c97c" /><br><br>
<img width="408" height="739" alt="image" src="https://github.com/user-attachments/assets/5cc2de40-8b7a-4cb1-a666-05bb9c6b6947" /><br><br>
<img width="414" height="840" alt="image" src="https://github.com/user-attachments/assets/0fc9f8df-09dd-4096-a06e-c2f853035d03" /><br><br>
<img width="368" height="183" alt="image" src="https://github.com/user-attachments/assets/0e375e01-a7f5-40f7-b9c1-234aebd63d4b" />


## Penjelasan Output
Saat program dijalankan akan muncul  
=== SISTEM ANTRIAN SPBU ===  
1. Kendaraan Masuk  
2. Kendaraan Selesai  
3. Lihat Antrian Depan  
4. Tampilkan Semua Antrian  
5. Keluar  
Pilih menu: ...  
<img width="384" height="208" alt="image" src="https://github.com/user-attachments/assets/1b7649bb-61c3-4717-b4e5-058513807b17" /><br> 
Disini saya menginputkan atau memilih pilihan 1, dan sistem menampilkan Masukkan nama/plat kendaraan:...  
lalu saya menginputkan Motor Revo  
lalu sistem menampilkan Kendaraan Motor Revo masuk Antrian  
<br><br>   
  
<img width="418" height="211" alt="image" src="https://github.com/user-attachments/assets/34021bc3-e84d-4b86-aa87-791c9976d175" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 1, dan sistem menampilkan Masukkan nama/plat kendaraan:...  
lalu saya menginputkan Motor Vario    
lalu sistem menampilkan Kendaraan Motor Vario masuk Antrian  
<br><br>   

<img width="414" height="213" alt="image" src="https://github.com/user-attachments/assets/8d6223c0-e6b6-4e31-9eea-35985e857bd1" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 1, dan sistem menampilkan Masukkan nama/plat kendaraan:...  
lalu saya menginputkan Motor Supra-X      
lalu sistem menampilkan Kendaraan Motor Supra-X masuk Antrian  
<br><br>   

<img width="357" height="201" alt="image" src="https://github.com/user-attachments/assets/dd4fda7f-f7ac-488a-8ea1-3be5c02e4727" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 3, dan sistem menampilkan  
Kendaraan paling depan: Motor Revo
<br><br>

<img width="351" height="283" alt="image" src="https://github.com/user-attachments/assets/145f9531-d946-4e05-a51c-39ac4d1ecbd1" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 4, dan sistem menampilkan  
Daftar Antrian kendaraan:
- Motor Revo
- Motor Vario
- Motor Supra-X  
<br><br>

<img width="406" height="197" alt="image" src="https://github.com/user-attachments/assets/764f7f80-0235-4357-9361-150e2afabfb4" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 2, dan sistem menampilkan    
Kendaraan Motor Revo selesai mengisi BBM
<br><br>

<img width="333" height="270" alt="image" src="https://github.com/user-attachments/assets/d8819425-4723-4cda-8442-82441461e2ad" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 4, dan sistem menampilkan      
Daftar Antrian kendaraan:
- Motor Vario
- Motor Supra-X
<br><br>

<img width="429" height="188" alt="image" src="https://github.com/user-attachments/assets/ba2272f1-bf55-4ca5-a884-1d57f5aeb1ed" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 2, dan sistem menampilkan      
Kendaraan Motor Vario selesai mengisi BBM
<br><br>

<img width="335" height="236" alt="image" src="https://github.com/user-attachments/assets/1cf3a4d4-6dc2-42d3-8147-b6de80c917a5" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 4, dan sistem menampilkan      
Daftar Antrian kendaraan:
- Motor Supra-X
<br><br>

<img width="438" height="204" alt="image" src="https://github.com/user-attachments/assets/902f7b7f-02d0-4468-b2a1-b61d69fea967" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 2, dan sistem menampilkan      
Kendaraan Motor Supra-X selesai mengisi BBM
<br><br>

<img width="295" height="199" alt="image" src="https://github.com/user-attachments/assets/df82da4f-6db0-48a1-b5e6-466853ade643" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 2, dan sistem menampilkan      
Antrian SPBU kosong
<br><br>

<img width="321" height="187" alt="image" src="https://github.com/user-attachments/assets/b2bacfc3-45cf-49b1-b28c-675b619164c7" /><br>
Lalu saya menginputkan atau memilih lagi pilihan 5, dan sistem menampilkan      
Program selesai  



## Link Video Presentasi YouTube
https://youtu.be/kSaW1G8YpRA
