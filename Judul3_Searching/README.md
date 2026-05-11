# Searching NPM Mahasiswa Menggunakan Interpolation Search

## A. Judul Program
**Program Pencarian NPM Mahasiswa Menggunakan Interpolation Search**
## Deskripsi Singkat

Program ini dibuat untuk melakukan pencarian data NPM mahasiswa Teknik Informatika pada sebuah list yang telah diurutkan secara ascending. User diminta memasukkan NPM yang ingin dicari, lalu program akan menentukan apakah data tersebut ada dalam daftar atau tidak.

Metode searching yang digunakan adalah Interpolation Search, yaitu algoritma pencarian yang bekerja dengan memperkirakan posisi data berdasarkan nilai target terhadap range data minimum dan maksimum. Metode ini lebih efisien dibandingkan sequential search pada data numerik yang terurut dan terdistribusi merata.


## Source Code
<img width="1772" height="2040" alt="searching2" src="https://github.com/user-attachments/assets/96cad1ce-4414-47c6-b90f-607a69b8c540" />


## Penjelasan Source Code
def interpolation_search(data, n, target):
Membuat fungsi interpolation search dengan parameter:
- `data` = list data NPM
- `n` = jumlah data
- `target` = data yang dicari


low = 0  
high = n - 1  
Menentukan indeks awal dan akhir.


while target >= data[low] and target <= data[high] and low <= high:  
Perulangan akan terus berjalan selama 3 kondisi terpenuhi:
1. `target >= data[low]`  
   Mengecek apakah nilai yang dicari lebih besar atau sama dengan nilai pada indeks awal (low).

2. `target <= data[high]`  
   Mengecek apakah nilai yang dicari lebih kecil atau sama dengan nilai pada indeks akhir (high).

3. `low <= high`  
   Memastikan indeks awal tidak melewati indeks akhir.  
Jika salah satu kondisi tidak terpenuhi, pencarian dihentikan karena target dipastikan tidak ada dalam rentang data.


if data[high] == data[low]:  
Mengecek apakah nilai pada indeks awal (low) dan indeks akhir (high) sama.  
Kondisi ini penting untuk menghindari pembagian dengan nol pada rumus interpolation search:


(target - data[low]) / (data[high] - data[low])  
Jika data[high sama dengan data[low], maka penyebut bernilai 0 dan program akan error.


if data[low] == target:  
Jika semua nilai dalam rentang sama, program mengecek apakah nilai tersebut sama dengan target yang dicari.


return low  
Jika target ditemukan, fungsi mengembalikan indeks low sebagai posisi data.


break  
Jika target tidak sama dengan nilai pada low, maka perulangan berhenti karena data tidak ditemukan.


pos = low + int(((target - data[low]) / (data[high] - data[low])) * (high - low))  
Menghitung posisi estimasi target menggunakan rumus interpolation search.


print(f"Posisi estimasi: {pos}, NPM: {data[pos]}")  
Menampilkan posisi estimasi sementara.


if target > data[pos]:  
    low = pos + 1  
Jika target lebih besar, geser pencarian ke kanan.


elif target < data[pos]:  
    high = pos - 1  
Jika target lebih kecil, geser pencarian ke kiri.


else:  
    return pos  
Jika target sama, kembalikan indeks.


return -1  
Jika tidak ditemukan, kembalikan -1.


def main():  
Mendefinisikan fungsi utama bernama main() sebagai tempat menjalankan program.


data = [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]  
Membuat list bernama data yang berisi kumpulan NPM mahasiswa yang sudah terurut ascending (dari kecil ke besar).


n = len(data)  
Menghitung jumlah elemen pada list data, lalu menyimpannya ke variabel n.


print(f"Daftar NPM Mahasiswa TI: {data}")   
Menampilkan seluruh daftar NPM yang tersedia pada program.


while True:  
Membuat perulangan tanpa batas sampai user memasukkan input yang valid.


try:  
Mencoba menjalankan kode yang berpotensi error.


target = int(input("Masukkan NPM yang ingin dicari: "))  
Meminta user memasukkan NPM yang ingin dicari, lalu mengubah input menjadi tipe data integer.


break  
Menghentikan perulangan jika input valid.


except ValueError:  
Menangkap error jika user memasukkan input selain angka.


print("Input tidak valid, masukkan angka!")  
Menampilkan pesan error apabila input bukan angka.


pos = interpolation_search(data, n, target)  
Memanggil fungsi interpolation_search() untuk mencari posisi NPM dalam list data.

- `data` = daftar NPM  
- `n` = jumlah data  
- `target` = NPM yang dicari  
Hasil pencarian disimpan ke variabel pos.


if pos != -1:  
Mengecek apakah data ditemukan.  
Jika hasil bukan -1, berarti target ada dalam list.


print(f"NPM {target} ditemukan pada indeks ke-{pos}")  
Menampilkan pesan bahwa NPM ditemukan beserta indeksnya.


else:  
Dijalankan jika data tidak ditemukan.


print(f"NPM {target} tidak ditemukan")  
Menampilkan pesan bahwa NPM tidak ada dalam list.


if __name__ == "__main__":  
Memastikan program hanya berjalan jika file dieksekusi langsung, bukan di-import dari file lain.


main()  
Memanggil fungsi main() untuk menjalankan seluruh program.

## Output Program
<img width="1136" height="532" alt="image" src="https://github.com/user-attachments/assets/d4be38e8-223b-4c72-b11c-be913de1ea16" />


## Penjelasan Output


```bash
Daftar NPM Mahasiswa TI: [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]
Masukkan NPM yang ingin dicari: A
Input tidak valid, masukkan angka!
Masukkan NPM yang ingin dicari: 2515061100
NPM 2515061100 tidak ditemukan
```
**Penjelasan:**
Program menampilkan daftar NPM yang tersedia. User memasukkan huruf A, padahal program hanya menerima angka. Muncul pesan error: Input tidak valid, masukkan angka! User memasukkan angka 2515061100. Karena NPM tersebut tidak ada dalam list, program menampilkan: NPM 2515061100 tidak ditemukan


**Output:**

```bash
Daftar NPM Mahasiswa TI: [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]
Masukkan NPM yang ingin dicari: 2515061005
Posisi estimasi: 0, NPM: 2515061005
NPM 2515061005 ditemukan pada indeks ke-0
```
**Penjelasan:**
User mencari NPM 2515061005. Algoritma menghitung posisi estimasi pertama pada indeks 0. Data pada indeks 0 cocok dengan target. Program menampilkan bahwa data ditemukan pada indeks ke-0.


**Output:**
```bash
Daftar NPM Mahasiswa TI: [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]
Masukkan NPM yang ingin dicari: 2515061067
Posisi estimasi: 3, NPM: 2515061050
Posisi estimasi: 4, NPM: 2515061067
NPM 2515061067 ditemukan pada indeks ke-4
```
**Penjelasan:**
User mencari NPM 2515061067. Estimasi pertama berada di indeks 3, tetapi data belum sesuai. Algoritma menghitung ulang posisi berikutnya ke indeks 4. Data pada indeks 4 cocok dengan target. Program menampilkan bahwa data ditemukan pada indeks ke-4.


**Output:**
```bash
Daftar NPM Mahasiswa TI: [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]
Masukkan NPM yang ingin dicari: 2515061099
Posisi estimasi: 6, NPM: 2515061099
NPM 2515061099 ditemukan pada indeks ke-6
```
**Penjelasan:**
User mencari NPM terakhir yaitu 2515061099. Algoritma langsung memperkirakan posisi pada indeks. Data sesuai dengan target. Program menampilkan bahwa data ditemukan pada indeks ke-6.

## Tugas Binary Interpolation
<img width="919" height="1280" alt="interpolation binary danish" src="https://github.com/user-attachments/assets/b2d56caf-9d7b-48c7-9e56-1219f34d3d04" />


## Link Video Presentasi YouTube







