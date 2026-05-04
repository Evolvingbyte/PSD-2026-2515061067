# Program Pengurutan Harga Barang Warung Madura

## A. Judul Program

**Program Pengurutan Harga Barang Warung Madura Menggunakan Bubble Sort**



## B. Deskripsi Singkat

Program ini merupakan program sederhana berbasis Python yang digunakan untuk mengurutkan data barang pada Warung Madura berdasarkan harga barang. Pengguna diminta untuk memasukkan jumlah barang, nama barang, dan harga barang. Setelah semua data dimasukkan, program akan menampilkan daftar barang sebelum diurutkan, daftar barang dari harga termurah ke harga termahal, dan daftar barang dari harga termahal ke harga termurah.

Algoritma yang digunakan pada program ini adalah Bubble Sort. Bubble Sort bekerja dengan cara membandingkan dua data yang bersebelahan, kemudian menukar posisinya jika data tersebut belum sesuai urutan. Pada program ini, Bubble Sort digunakan untuk mengurutkan harga barang dari yang paling murah ke yang paling mahal. Untuk menampilkan data dari harga termahal ke termurah, program menggunakan fungsi `reversed()` untuk membalik hasil urutan yang sudah dibuat.



## C. Source Code

Berikut adalah gambar source code program:

<img width="623" height="612" alt="Screenshot 2026-05-04 225941" src="https://github.com/user-attachments/assets/41410721-2131-4d52-ab2e-ad78a757951d" />

<img width="780" height="674" alt="Screenshot 2026-05-04 230005" src="https://github.com/user-attachments/assets/bd79028d-d94e-4c14-9cdb-25ce4355c292" />

### Penjelasan Logika Source Code Per Baris

#### 1. Fungsi `tukar`

def tukar(arr, i, j):
Baris ini membuat fungsi bernama `tukar`. Fungsi ini digunakan untuk menukar posisi dua data di dalam list.


    temp = arr[i]
Baris ini menyimpan data pada indeks ke-`i` ke dalam variabel sementara bernama `temp`.


    arr[i] = arr[j]
Baris ini mengganti data pada indeks ke-`i` dengan data yang ada pada indeks ke-`j`.


    arr[j] = temp
Baris ini mengganti data pada indeks ke-`j` dengan data yang sebelumnya disimpan di variabel `temp`. Dengan begitu, data pada indeks `i` dan `j` berhasil ditukar.


def bubble_sort_harga(barang, n):
Baris ini membuat fungsi bernama `bubble_sort_harga`. Fungsi ini digunakan untuk mengurutkan data barang berdasarkan harga dari yang termurah ke yang termahal.


    for i in range(n - 1):
Baris ini membuat perulangan pertama. Perulangan ini digunakan untuk menentukan berapa kali proses pengurutan dilakukan.


        for j in range(n - i - 1):
Baris ini membuat perulangan kedua. Perulangan ini digunakan untuk membandingkan harga barang yang bersebelahan.


            if barang[j]["harga"] > barang[j + 1]["harga"]:
Baris ini mengecek apakah harga barang pada posisi sekarang lebih besar daripada harga barang setelahnya. Jika iya, maka posisi kedua barang tersebut harus ditukar agar harga yang lebih murah berada di depan.


                tukar(barang, j, j + 1)
Baris ini memanggil fungsi `tukar` untuk menukar posisi dua barang yang sedang dibandingkan.


def main():
Baris ini membuat fungsi utama program. Semua proses utama program dijalankan di dalam fungsi `main`.


    try:
Baris ini digunakan untuk mencoba menjalankan kode yang kemungkinan dapat menghasilkan error.


        n = int(input("Masukkan jumlah barang: "))
Baris ini meminta pengguna memasukkan jumlah barang. Input yang dimasukkan akan diubah menjadi tipe data integer menggunakan `int`.


    except ValueError:
Baris ini digunakan untuk menangkap error apabila pengguna memasukkan input yang bukan angka.


        print("Input tidak valid!")
Baris ini menampilkan pesan bahwa input yang dimasukkan tidak valid.


        return
Baris ini menghentikan program jika input jumlah barang tidak valid.


    barang = []
Baris ini membuat list kosong bernama `barang`. List ini digunakan untuk menyimpan data barang yang dimasukkan oleh pengguna.

    print("\nMasukkan data barang Warung Madura:")
Baris ini menampilkan teks informasi bahwa pengguna akan memasukkan data barang Warung Madura.


    for i in range(n):
Baris ini membuat perulangan sebanyak jumlah barang yang sudah dimasukkan pengguna.


        print(f"\nBarang ke-{i + 1}")
Baris ini menampilkan urutan barang, misalnya Barang ke-1, Barang ke-2, dan seterusnya.


        nama = input("Nama barang: ")
Baris ini meminta pengguna memasukkan nama barang.


        while True:
Baris ini membuat perulangan yang terus berjalan sampai pengguna memasukkan harga barang yang benar.


            try:
Baris ini digunakan untuk mencoba menjalankan proses input harga barang.


                harga = int(input("Harga barang: "))
Baris ini meminta pengguna memasukkan harga barang. Input harga akan diubah menjadi angka menggunakan `int`.


                barang.append({
Baris ini digunakan untuk menambahkan data barang ke dalam list `barang`.


                    "nama": nama,
Baris ini menyimpan nama barang ke dalam dictionary dengan key `"nama"`.


                    "harga": harga
Baris ini menyimpan harga barang ke dalam dictionary dengan key `"harga"`.


                break
Baris ini menghentikan perulangan `while` jika harga barang berhasil dimasukkan dengan benar.


            except ValueError:
Baris ini menangkap error jika pengguna memasukkan harga yang bukan angka.


                print("Input harga tidak valid, silakan masukkan angka!")
Baris ini menampilkan pesan bahwa input harga tidak valid, sehingga pengguna harus memasukkan angka.



    print("\nDaftar barang sebelum diurutkan:")
Baris ini menampilkan judul daftar barang sebelum dilakukan proses pengurutan.


    for item in barang:
Baris ini melakukan perulangan untuk mengambil setiap data barang yang ada di dalam list `barang`.


        print(f"{item['nama']} - Rp{item['harga']}")
Baris ini menampilkan nama barang dan harga barang sebelum diurutkan.



    bubble_sort_harga(barang, n)
Baris ini memanggil fungsi `bubble_sort_harga` untuk mengurutkan data barang berdasarkan harga dari yang termurah ke yang termahal.


    print("\nDaftar barang setelah diurutkan berdasarkan harga termurah:")
Baris ini menampilkan judul daftar barang setelah diurutkan berdasarkan harga termurah.


    for item in barang:
Baris ini melakukan perulangan untuk mengambil setiap data barang yang sudah diurutkan.


        print(f"{item['nama']} - Rp{item['harga']}")
Baris ini menampilkan nama barang dan harga barang dari yang paling murah ke yang paling mahal.


    print("\nDaftar barang setelah diurutkan berdasarkan harga termahal:")
Baris ini menampilkan judul daftar barang setelah diurutkan berdasarkan harga termahal.


    for item in reversed(barang):
Baris ini digunakan untuk menampilkan isi list `barang` secara terbalik. Karena sebelumnya data sudah diurutkan dari harga termurah ke harga termahal, maka ketika menggunakan `reversed(barang)`, data akan tampil dari harga termahal ke harga termurah.


        print(f"{item['nama']} - Rp{item['harga']}")
Baris ini menampilkan nama barang dan harga barang dari yang paling mahal ke yang paling murah.



if __name__ == "__main__":
Baris ini digunakan untuk mengecek apakah file Python dijalankan secara langsung.


        main()
Baris ini memanggil fungsi `main`, sehingga program mulai dijalankan.



## D. Output Program

Berikut adalah gambar output program:

<img width="340" height="520" alt="image" src="https://github.com/user-attachments/assets/ea17890c-718e-43eb-90e2-6992d119e035" />
<img width="558" height="448" alt="image" src="https://github.com/user-attachments/assets/615c18b3-3a15-41eb-977d-7b4c0cb9f21c" />


### Penjelasan Output

Pada contoh output di atas, pengguna memasukkan jumlah barang sebanyak 5 barang. Data barang yang dimasukkan adalah Indomie dengan harga Rp5000, minyak goreng dengan harga Rp35000, garam dengan harga Rp3500,  kecap dengan harga Rp8000, dan sabun cuci piring dengan harga Rp10000.

Program pertama-tama menampilkan daftar barang sebelum diurutkan. Daftar ini masih sesuai dengan urutan input dari pengguna. Setelah itu, program mengurutkan data barang menggunakan algoritma Bubble Sort berdasarkan harga dari yang paling murah ke yang paling mahal.

Hasil pengurutan dari harga termurah adalah Indomie, Kopi, Gula, lalu Beras. Indomie berada di urutan pertama karena memiliki harga paling murah, sedangkan Beras berada di urutan terakhir karena memiliki harga paling mahal.

Selanjutnya, program menampilkan daftar barang berdasarkan harga termahal. Pada bagian ini, program menggunakan fungsi `reversed(barang)` untuk membalik urutan data yang sudah diurutkan sebelumnya. Hasilnya, Beras tampil di urutan pertama karena memiliki harga paling mahal, kemudian Gula, Kopi, dan terakhir Indomie sebagai barang dengan harga paling murah.

Dengan demikian, program berhasil berjalan sesuai studi kasus tanpa error dan mampu menampilkan data barang dalam dua urutan, yaitu dari harga termurah ke harga termahal dan dari harga termahal ke harga termurah.



## E. Link YouTube

Berikut adalah link video presentasi atau demo program:

[[Link Video YouTube](https://youtube.com/)](https://youtu.be/W_bFxg2PdB8)
