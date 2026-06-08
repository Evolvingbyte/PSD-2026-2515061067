# Sistem Parkir Menggunakan Hash Table dengan Linear Probing

## Judul Program

**Program Sistem Parkir Menggunakan Hash Table dengan Linear Probing**

## Deskripsi Singkat

Program ini dibuat untuk mengelola data kendaraan yang masuk dan keluar dari area parkir menggunakan struktur data Hash Table. Setiap kendaraan memiliki nomor tiket sebagai key dan nomor polisi sebagai value.

Untuk mengatasi collision (dua data memiliki indeks hash yang sama), program menggunakan metode Linear Probing. Jika slot yang dituju sudah terisi, maka sistem akan mencari slot berikutnya secara berurutan hingga menemukan slot kosong.

Fitur yang tersedia pada program:

* Menambahkan kendaraan ke area parkir.
* Mencari kendaraan berdasarkan nomor tiket.
* Mengeluarkan kendaraan dari parkiran.
* Menampilkan seluruh status slot parkir.

Metode Hash Table dipilih karena memiliki proses pencarian dan penyimpanan data yang cepat.


# Source Code

<img width="1662" height="4434" alt="TA judul 6 source code" src="https://github.com/user-attachments/assets/f61023e8-a32a-4174-802c-f948e5fa592f" />



# Penjelasan Source Code

class SlotState:  
Membuat class yang digunakan untuk menyimpan status setiap slot pada hash table.   

EMPTY = 0  
Status slot kosong dan belum pernah digunakan.  

OCCUPIED = 1  
Status slot sedang digunakan kendaraan.  

DELETED = 2  
Status slot pernah digunakan tetapi kendaraan sudah keluar.  

class Entry:  
Membuat class untuk menyimpan data pada setiap slot hash table.  

def init(self):  
Constructor yang akan dijalankan ketika objek Entry dibuat.  

self.nomor_polisi = None  
Menyimpan nomor polisi kendaraan.  

self.nomor_tiket = None  
Menyimpan nomor tiket kendaraan.  

self.state = SlotState.EMPTY   
Status awal slot adalah kosong.   

class SistemParkir:  
Class utama yang digunakan untuk mengelola seluruh sistem parkir.  

def **init**(self, jumlah_slot=10):  
Constructor untuk membuat hash table.  

self.jumlah_slot = jumlah_slot   
Menyimpan jumlah slot parkir yang tersedia.   

self.table = [Entry() for _ in range(jumlah_slot)]   
Membuat list yang berisi objek Entry sebanyak jumlah slot.   

def hash_function(self, nomor_tiket):   
Fungsi hash yang digunakan untuk menentukan indeks penyimpanan data.   

return nomor_tiket % self.jumlah_slot    
Menggunakan operasi modulo.   

def parkir_masuk(self, nomor_tiket, nomor_polisi):   
Digunakan untuk menambahkan kendaraan ke parkiran.   

index = self.hash_function(nomor_tiket)    
Menghitung indeks awal menggunakan fungsi hash.   

for step in range(self.jumlah_slot):   
Melakukan perulangan untuk proses Linear Probing.   
Perulangan dilakukan maksimal sebanyak jumlah slot.  

i = (index + step) % self.jumlah_slot   
Menghitung posisi yang akan diperiksa.   

if self.table[i].state in (SlotState.EMPTY, SlotState.DELETED):   
Memeriksa apakah slot kosong atau pernah digunakan.    
Jika iya maka slot dapat digunakan untuk menyimpan kendaraan baru.   

self.table[i].nomor_tiket = nomor_tiket    
Menyimpan nomor tiket kendaraan.    

self.table[i].nomor_polisi = nomor_polisi   
Menyimpan nomor polisi kendaraan.   

self.table[i].state = SlotState.OCCUPIED   
Mengubah status slot menjadi terisi.   

print(f"Kendaraan {nomor_polisi} parkir di slot {i}")   
Menampilkan informasi slot tempat kendaraan parkir.   

return True   
Menandakan proses parkir berhasil.   

print("Parkiran penuh!")    
Dijalankan jika seluruh slot sudah terisi.   

return False  
Menandakan kendaraan gagal masuk karena tidak ada slot kosong.   

def cari_kendaraan(self, nomor_tiket):    
Digunakan untuk mencari kendaraan berdasarkan nomor tiket.   

index = self.hash_function(nomor_tiket)   
Menghitung indeks awal pencarian.   

for step in range(self.jumlah_slot):   
Melakukan Linear Probing untuk pencarian data.   

i = (index + step) % self.jumlah_slot   
Menghitung slot yang sedang diperiksa.   

if self.table[i].state == SlotState.EMPTY:   
Jika menemukan slot kosong maka data tidak ditemukan.   

return None   
Mengembalikan nilai None karena kendaraan tidak ada.   

if (  
    self.table[i].state == SlotState.OCCUPIED and   
    self.table[i].nomor_tiket == nomor_tiket   
)   
Memeriksa apakah slot terisi dan nomor tiket sesuai.   

return i    
Mengembalikan nomor slot tempat kendaraan berada.   

return None  
Dijalankan jika seluruh proses pencarian selesai tetapi data tidak ditemukan.   

def kendaraan_keluar(self, nomor_tiket):    
Digunakan untuk mengeluarkan kendaraan dari parkiran.   

slot = self.cari_kendaraan(nomor_tiket)   
Mencari posisi kendaraan berdasarkan nomor tiket.   

if slot is not None:   
Memeriksa apakah kendaraan ditemukan.   

print(   
f"Kendaraan {self.table[slot].nomor_polisi}   
keluar dari slot {slot}"   
Menampilkan informasi kendaraan yang keluar.   

self.table[slot].state = SlotState.DELETED   
Mengubah status slot menjadi DELETED.   
Status tidak diubah menjadi EMPTY karena dapat merusak proses pencarian data lain yang mengalami collision.   

return True    
Menandakan proses keluar berhasil.   

print("Kendaraan tidak ditemukan")   
Dijalankan jika nomor tiket tidak ditemukan.   

return False   
Menandakan proses gagal.   

def tampilkan_parkiran(self):   
Digunakan untuk menampilkan seluruh isi parkiran.   

print("\n=== STATUS PARKIRAN ===")   
Menampilkan judul tampilan parkiran.   

for i in range(self.jumlah_slot):   
Melakukan perulangan dari slot pertama hingga slot terakhir.   

print(f"Slot {i}: ", end="")   
Menampilkan nomor slot.  

if self.table[i].state == SlotState.EMPTY:  
Memeriksa apakah slot kosong.  

print("Kosong")   
Menampilkan status kosong.   

elif self.table[i].state == SlotState.DELETED:   
Memeriksa apakah slot pernah digunakan.   

print("Pernah Terisi")   
Menampilkan status pernah terisi.   

else:  
Dijalankan jika slot sedang digunakan.   

print(   
f"{self.table[i].nomor_polisi}   
(Tiket {self.table[i].nomor_tiket})"   
)   
Menampilkan nomor polisi dan nomor tiket kendaraan.   

def main():   
Fungsi utama program.  
 
parkir = SistemParkir(10)   
Membuat objek parkir dengan kapasitas 10 slot.   

parkir.parkir_masuk(1, "BE1234AA")   
Menambahkan kendaraan pertama.  

parkir.parkir_masuk(11, "BE5678BB")   
Terjadi collision dengan tiket 1.   
Linear Probing mencari slot berikutnya sehingga kendaraan masuk ke slot 2.   

parkir.parkir_masuk(21, "BE9012CC")    
Terjadi collision lagi.   
Masuk ke slot 3.   

parkir.parkir_masuk(2, "BE3456DD")   
Slot 2 dan slot 3 sudah terisi sehingga kendaraan masuk ke slot 4.   

parkir.tampilkan_parkiran()    
Menampilkan seluruh status parkiran.   

slot = parkir.cari_kendaraan(11)   
Mencari kendaraan dengan tiket nomor 11.   

if slot is not None:   
Memeriksa apakah kendaraan ditemukan.   

print(f"Kendaraan ditemukan di slot {slot}")   
Menampilkan posisi kendaraan.   

else:    
Dijalankan jika kendaraan tidak ditemukan.   

print("Kendaraan tidak ditemukan")    
Menampilkan pesan gagal.    

parkir.kendaraan_keluar(11)    
Mengeluarkan kendaraan dengan tiket 11.   

parkir.tampilkan_parkiran()   
Menampilkan kondisi parkiran setelah kendaraan keluar.    


if name == "main":   
Digunakan untuk memastikan program hanya dijalankan ketika file dieksekusi secara langsung.   

main()   
Menjalankan fungsi utama program.   


# Output Program

<img width="377" height="755" alt="image" src="https://github.com/user-attachments/assets/a5f06e87-c760-4a73-be52-173d2db600d0" />


# Penjelasan Output
Kendaraan pertama memiliki nomor polisi BE1234AA dengan nomor tiket 1. Hasil hash dari 1 % 10 adalah 1 sehingga kendaraan ditempatkan pada slot 1.

Selanjutnya kendaraan kedua memiliki nomor polisi BE5678BB dengan nomor tiket 11. Hasil hash dari 11 % 10 juga menghasilkan indeks 1. Karena slot 1 sudah terisi oleh kendaraan pertama, terjadi collision. Program menggunakan metode Linear Probing untuk mencari slot kosong berikutnya dan menemukan slot 2. Oleh karena itu kendaraan kedua ditempatkan pada slot 2.

Kendaraan ketiga memiliki nomor polisi BE9012CC dengan nomor tiket 21. Hasil hash dari 21 % 10 kembali menghasilkan indeks 1. Karena slot 1 dan slot 2 sudah terisi, program melakukan Linear Probing hingga menemukan slot 3 yang masih kosong. Kendaraan kemudian ditempatkan pada slot 3.

Kendaraan keempat memiliki nomor polisi BE3456DD dengan nomor tiket 2. Hasil hash dari 2 % 10 adalah 2. Namun slot 2 sudah terisi oleh kendaraan kedua dan slot 3 sudah terisi oleh kendaraan ketiga. Program kembali melakukan Linear Probing hingga menemukan slot 4 yang kosong sehingga kendaraan ditempatkan pada slot 4.

Setelah seluruh kendaraan berhasil masuk, program menampilkan kondisi seluruh slot parkir. Terlihat bahwa slot 1, 2, 3, dan 4 berisi kendaraan, sedangkan slot lainnya masih kosong.

Selanjutnya program melakukan pencarian kendaraan menggunakan nomor tiket 11. Sistem menghitung indeks hash dan melakukan proses pencarian hingga menemukan kendaraan dengan tiket 11 pada slot 2. Oleh karena itu program menampilkan pesan bahwa kendaraan ditemukan di slot 2.

Setelah proses pencarian selesai, kendaraan dengan nomor polisi BE5678BB dan nomor tiket 11 dikeluarkan dari area parkir. Program menampilkan informasi bahwa kendaraan keluar dari slot 2.

Saat kendaraan keluar, status slot tidak diubah menjadi Kosong, tetapi menjadi Pernah Terisi (DELETED). Hal ini dilakukan agar proses pencarian kendaraan lain yang mengalami collision tetap dapat berjalan dengan benar.

Terakhir, program kembali menampilkan kondisi parkiran setelah kendaraan keluar. Pada tampilan tersebut terlihat bahwa slot 2 berubah menjadi Pernah Terisi, sedangkan kendaraan lain masih berada pada slot masing-masing. Slot 0, 5, 6, 7, 8, dan 9 tetap dalam keadaan kosong.



## Link Video Presentasi YouTube
https://youtu.be/2t9PB8UlVt0

