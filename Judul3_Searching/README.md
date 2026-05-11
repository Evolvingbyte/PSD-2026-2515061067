# Searching NPM Mahasiswa Menggunakan Interpolation Search

## A. Judul Program
**Program Pencarian NPM Mahasiswa Menggunakan Interpolation Search**
## Deskripsi Singkat

Program ini dibuat untuk melakukan pencarian data NPM mahasiswa Teknik Informatika pada sebuah list yang telah diurutkan secara ascending. User diminta memasukkan NPM yang ingin dicari, lalu program akan menentukan apakah data tersebut ada dalam daftar atau tidak.

Metode searching yang digunakan adalah Interpolation Search, yaitu algoritma pencarian yang bekerja dengan memperkirakan posisi data berdasarkan nilai target terhadap range data minimum dan maksimum. Metode ini lebih efisien dibandingkan sequential search pada data numerik yang terurut dan terdistribusi merata.


## Source Code
<img width="1772" height="2040" alt="searching2" src="https://github.com/user-attachments/assets/96cad1ce-4414-47c6-b90f-607a69b8c540" />


## Penjelasan Source Code
#def interpolation_search(data, n, target):
Membuat fungsi interpolation search dengan parameter:
- `data` = list data NPM
- `n` = jumlah data
- `target` = data yang dicari


low = 0
high = n - 1
Menentukan indeks awal dan akhir.


while target >= data[low] and target <= data[high] and low <= high:
Perulangan dilakukan selama target masih dalam range data.


if data[high] == data[low]:
Mengecek jika semua data pada range sama.


pos = low + int(((target - data[low]) / (data[high] - data[low])) * (high - low))
Menghitung posisi estimasi target menggunakan rumus interpolation search.






