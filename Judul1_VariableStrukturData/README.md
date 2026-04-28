#  Sistem Pesanan Makanan (Linked List)

## a. Judul Program
Sistem Pesanan Makanan Menggunakan Linked List

## b. Deskripsi Singkat
Program ini dibuat untuk mengelola daftar pesanan makanan menggunakan struktur data **Linked List**. Pengguna dapat menambahkan pesanan, melihat daftar pesanan, dan memproses pesanan pertama.

Algoritma yang digunakan adalah **Single Linked List** dengan konsep **FIFO (First In First Out)**, di mana pesanan yang pertama masuk akan diproses terlebih dahulu. Program ini juga menerapkan **exception handling** untuk menangani input yang tidak valid.


## c. Source Code

###  Screenshot Source Code
Tambahkan gambar source code di bawah ini:
<img width="536" height="854" alt="image" src="https://github.com/user-attachments/assets/113ac8fd-d0f2-475f-b191-4281fec5f9b1" />
<img width="662" height="812" alt="image" src="https://github.com/user-attachments/assets/77263d6a-9225-402d-ac76-45119f030793" />
<img width="467" height="318" alt="image" src="https://github.com/user-attachments/assets/0218e135-cf04-40dc-8e52-a603ce8e3391" />


###  Penjelasan Kode
1. **Class Node**
   - Digunakan untuk menyimpan data pesanan
   - Memiliki atribut:
     - `pesanan` → menyimpan nama makanan
     - `next` → menunjuk ke node berikutnya

2. **Class LinkedList**
   - `__init__()`  
     Menginisialisasi head sebagai None
   - `tambah_pesanan(pesanan)`  
     Membuat node baru, lalu:
     - Jika list kosong → jadi head
     - Jika tidak → ditambahkan di akhir
   - `tampilkan_pesanan()`  
     Menampilkan semua data dengan perulangan dari head sampai akhir
   - `proses_pesanan()`  
     Menghapus node pertama (head) dan memindahkan ke node berikutnya

3. **Fungsi menu()**
   - Menampilkan pilihan menu ke user

4. **Fungsi main()**
   - Menggunakan perulangan `while True`
   - Input user diproses dengan `try-except`
   - Menjalankan fungsi sesuai pilihan menu


## d. Output Program
<img width="317" height="749" alt="image" src="https://github.com/user-attachments/assets/d753c454-e163-4834-83e5-d016a7ba2e52" />
<img width="369" height="631" alt="image" src="https://github.com/user-attachments/assets/449bfcfd-4f06-473d-8de3-e42ef9d4ec0b" />
<img width="384" height="402" alt="image" src="https://github.com/user-attachments/assets/0b990b75-79d9-4d65-8afa-dc2fd4b1fd25" />


###  Screenshot Output
<img width="373" height="767" alt="image" src="https://github.com/user-attachments/assets/2c912f8f-508c-4e84-89b7-e069053ce815" />
<img width="385" height="782" alt="image" src="https://github.com/user-attachments/assets/c50250e3-deee-4f2f-90d6-eaffdc1b1c4c" />
<img width="417" height="374" alt="image" src="https://github.com/user-attachments/assets/01967aac-be48-49c4-bb50-0c3d419a6434" />


###  Penjelasan Output
- Saat user memasukkan huruf → muncul pesan **"Input harus angka!"**
- Saat memilih menu tidak tersedia → muncul **"Pilihan tidak valid!"**
- Saat menambah pesanan → data masuk ke Linked List
- Saat menampilkan → semua pesanan ditampilkan berurutan
- Saat memproses → pesanan pertama dihapus (FIFO)


## e. Link YouTube
https://youtu.be/NYUfs-jxDTU






