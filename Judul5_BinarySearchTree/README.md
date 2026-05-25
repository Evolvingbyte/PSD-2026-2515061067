# Sistem Kursi Bioskop Menggunakan Binary Search Tree (BST)

## Judul Program
**Program Sistem Kursi Bioskop Menggunakan Binary Search Tree (BST)**

## Deskripsi Singkat
Program ini dibuat untuk mengelola pemesanan kursi bioskop menggunakan struktur data Binary Search Tree (BST). User dapat memesan kursi, mencari status kursi, menampilkan daftar kursi secara terurut, menghitung jumlah kursi yang telah dipesan, serta melihat kursi pertama dan kursi terakhir yang telah terisi.

Metode BST digunakan agar proses pencarian dan penyimpanan data kursi menjadi lebih cepat dan terstruktur. Setiap nomor kursi akan disimpan berdasarkan aturan BST, yaitu:
- Data yang lebih kecil disimpan di subtree kiri.  
- Data yang lebih besar disimpan di subtree kanan.    
Program juga menggunakan exception handling untuk menangani input yang tidak valid.


# Source Code
<img width="1524" height="4662" alt="source code TA5 terbaru" src="https://github.com/user-attachments/assets/3c616915-ef51-423c-a5d3-66d5ca71718a" />


# Penjelasan Source Code
class Node:  
Membuat class Node untuk menyimpan data kursi pada Binary Search Tree.


def __init__(self, nomor_kursi):  
Fungsi constructor untuk menginisialisasi node.

self.nomor_kursi = nomor_kursi   
Menyimpan nomor kursi ke dalam node.

self.left = None  
Pointer ke subtree kiri.

self.right = None  
Pointer ke subtree kanan.


class BioskopBST:   
Class utama untuk mengelola Binary Search Tree kursi bioskop.


def __init__(self):   
Inisialisasi BST.


self.root = None   
Root awal masih kosong.

def insert_node(self, root, nomor_kursi):   
Digunakan untuk menambahkan kursi ke BST.


if root is None:  
    return Node(nomor_kursi)  
Jika node kosong maka membuat node baru.


if nomor_kursi < root.nomor_kursi:  
Jika data lebih kecil maka masuk ke subtree kiri.

root.left = self.insert_node(root.left, nomor_kursi)  
Masukkan ke subtree kiri.

elif nomor_kursi > root.nomor_kursi:  
Jika data lebih besar maka masuk ke subtree kanan.

root.right = self.insert_node(root.right, nomor_kursi)  
Masukkan ke subtree kanan.

else:  
    print("Kursi sudah dipesan!")   
Jika data sama maka menampilkan kursi sudah terisi.

return root  
Mengembalikan node root setelah proses insert selesai.


def pesan_kursi(self, nomor_kursi):  
Fungsi untuk memesan kursi.


self.root = self.insert_node(self.root, nomor_kursi)   
Memasukkan kursi ke BST.

def search_node(self, root, nomor_kursi):   
Digunakan untuk mencari kursi.


if root is None:  
    return False   
Jika node kosong berarti kursi tidak ditemukan.


if root.nomor_kursi == nomor_kursi:   
    return True   
Jika ditemukan maka mengembalikan True.


if nomor_kursi < root.nomor_kursi:    
Jika nomor kursi lebih kecil 

return self.search_node(root.left, nomor_kursi)    
Cari di subtree kiri.

return self.search_node(root.right, nomor_kursi)   
Cari ke subtree kanan.

def cari_kursi(self, nomor_kursi):   
Fungsi untuk menjalankan pencarian kursi.


return self.search_node(self.root, nomor_kursi)  
Memulai pencarian dari root.

def inorder(self, root):  
Digunakan untuk menampilkan kursi secara terurut.

self.inorder(root.left)  
Menampilkan subtree kiri.

if root is None:    
Jika node kosong.  

return    
Hentikan rekursi.    

self.inorder(root.left)   
Kunjungi subtree kiri.

print(root.nomor_kursi, end=" ")  
Menampilkan node sekarang.  


self.inorder(root.right)  
Menampilkan subtree kanan.

def count_nodes(self, root):  
Digunakan untuk menghitung jumlah kursi terisi.

if root is None:  
    return 0  
Jika kosong maka jumlah 0.


return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)  
Menghitung seluruh node BST.


def find_min(self, root):  
Digunakan untuk mencari kursi pertama.


if root is None:  
Jika tree kosong.

return None  
iMengembalikan tidak ada data.

current = root  
Simpan root ke variabel current.

while current.left is not None:   
Selama masih ada cabang kiri.

current = current.left  
Geser ke kiri terus.

return current.nomor_kursi   
Node paling kiri adalah nilai minimum.


def find_max(self, root):  
Digunakan untuk mencari kursi terakhir.

if root is None:  
Jika tree kosong.
           
return None  
Tidak ada data.


current = root  
Simpan root.

while current.right is not None:   
Selama masih ada cabang kanan.

current = current.right  
Geser ke kanan terus.

return current.nomor_kursi  
Node paling kanan adalah nilai maksimum.


def main():  
Fungsi utama program.

bioskop = BioskopBST()    
Membuat objek BST.

pilih = 0  
Variabel menu pilihan.
 
while pilih != 7:  
Perulangan menu program.

print("\n=== SISTEM KURSI BIOSKOP ===")   
Menampilkan judul menu.

 
print("1. Pesan Kursi")   
Menu memesan kursi.

 
print("2. Cari Kursi")   
Menu mencari kursi.


print("3. Tampilkan Kursi Terurut")   
Menu menampilkan kursi terurut.

 
print("4. Jumlah Kursi Terisi")  
Menu menghitung jumlah kursi terisi.

 
print("5. Kursi Pertama")  
Menu melihat kursi pertama.

 
print("6. Kursi Terakhir")   
Menu melihat kursi terakhir.

 
print("7. Keluar")   
Menu keluar program.

 
try: 
Mencoba input user.  

pilih = int(input("Pilih menu: "))   
Input pilihan menu.
 
except ValueError:   
Menangani error jika input bukan angka.

 
print("Input harus angka!")   
Menampilkan pesan error.

continue  
Kembali ke awal loop.

if pilih == 1:  
Jika pilih pesan kursi.

kursi = input("Masukkan nomor kursi: ").upper()   
Input nomor kursi dan ubah ke huruf besar.

if bioskop.cari_kursi(kursi):  
Cek apakah kursi sudah ada.

print("Kursi sudah dipesan!")   
Jika ada.
    
else:  
Jika belum ada.

bioskop.pesan_kursi(kursi)  
Simpan kursi ke BST.

print(f"Kursi {kursi} berhasil dipesan.")  
Tampilkan berhasil.

elif pilih == 2:  
Cari kursi.
            
kursi = input("Cari nomor kursi: ").upper()  
Input nomor kursi.

if bioskop.cari_kursi(kursi):     
Jika ditemukan.
               
print(f"Kursi {kursi} sudah terisi.")   
Tampilkan terisi.
            
else:    
Jika tidak ditemukan.

print(f"Kursi {kursi} masih kosong.")      
Tampilkan kosong.

elif pilih == 3:   
Menampilkan kursi terurut.

print("Daftar kursi terurut: ", end="")      
Cetak judul.

bioskop.inorder(bioskop.root)   
Traversal inorder.

print()   
Pindah baris.

elif pilih == 4:   
Menghitung jumlah kursi.

print(f"Jumlah kursi terisi: {bioskop.count_nodes(bioskop.root)}")   
Cetak total node.

elif pilih == 5:  
Menampilkan kursi minimum.

print(f"Kursi pertama: {bioskop.find_min(bioskop.root)}")   
Cetak kursi terkecil.

elif pilih == 6:  
Menampilkan kursi maksimum.

print(f"Kursi terakhir: {bioskop.find_max(bioskop.root)}")   
Cetak kursi terbesar.

elif pilih == 7:  
Jika user memilih keluar.

print("Program selesai.")     
Program selesai.

else:   
Jika input tidak valid.

print("Pilihan tidak valid!")   
Menampilkan pesan error.

if __name__ == "__main__":   
Mengecek apakah file dijalankan langsung.

main()    
Menjalankan fungsi utama main().
 

# Output Program
<img width="289" height="798" alt="image" src="https://github.com/user-attachments/assets/646b3025-05b6-4247-9ed8-29cd31287863" /><br><br>
<img width="302" height="788" alt="image" src="https://github.com/user-attachments/assets/8928d54d-c752-442d-a120-66d4ea83d7ce" /><br><br>
<img width="296" height="790" alt="image" src="https://github.com/user-attachments/assets/d6e477b9-003c-4fa5-963a-1df0744e9408" /><br><br>
<img width="454" height="732" alt="image" src="https://github.com/user-attachments/assets/8e41e8ae-f5b8-4bd6-a755-81aa840876c7" /><br><br>
<img width="300" height="775" alt="image" src="https://github.com/user-attachments/assets/3816a2da-f2bf-4006-b52c-aa1041355070" /><br><br>
<img width="284" height="495" alt="image" src="https://github.com/user-attachments/assets/2425b8b3-1952-4f5f-b454-040e6293dd5a" /><br><br>

# Penjelasan Output
<img width="289" height="798" alt="Screenshot 2026-05-25 210730" src="https://github.com/user-attachments/assets/f33d5935-1c4b-417f-a295-630e88af8e04" /><br><br>
Pada saat kode dijalankan muncul  
=== SISTEM KURSI BIOSKOP ===  
1. Pesan Kursi  
2. Cari Kursi  
3. Tampilkan Kursi Terurut  
4. Jumlah Kursi Terisi  
5. Kursi Pertama  
6. Kursi Terakhir   
7. Keluar  
Pilih menu:...

Saya memilih menu 1. Pesan Kursi, untuk memesan kursi bioskop satu persatu.    
Kursi yang dipesan adalah:    
- A5
- A2
- B3  
Setelah masing-masing nomor kursi dimasukkan, program menampilkan kursi tersebut berhasil   dipesan.  

<img width="302" height="788" alt="Screenshot 2026-05-25 210828" src="https://github.com/user-attachments/assets/ec45bf6f-49ed-444b-8c89-d8b755b83334" /><br><br>
lalu saya kembali memilih menu 1. Pesan Kursi,  untuk menambahkan kursi baru.   
Kursi yang dipesan adalah:    
- A1
- B5
- G7

<img width="296" height="790" alt="Screenshot 2026-05-25 210917" src="https://github.com/user-attachments/assets/0c3d31ab-a245-4304-82cb-3f539c1dbd48" /><br><br>
lalu saya masih menggunakan menu 1. Pesan Kursi, untuk melakukan pemesanan kursi.  
Kursi yang dipesan adalah:  
- B2
- G8
- G3

<img width="454" height="732" alt="Screenshot 2026-05-25 210949" src="https://github.com/user-attachments/assets/9fb406e9-be29-418f-b25b-0d73e5cc181f" /><br><br>
Lalu saya memilih beberapa menu untuk melihat data kursi yang sudah dipesan.
Pertama, memilih menu 3. Tampilkan Kursi Terurut. Program menampilkan daftar kursi yang sudah dipesan dalam kondisi sudah terurut (A1 A2 A5 B2 B3 B5 G3 G7 G8). Lalu saya memilih menu 4. Jumlah Kursi Terisi. Program menampilkan jumlah total kursi yang sudah dipesan adalah 9. Lalu saya memilih menu 5. Kursi Pertama. Program menampilkan kursi pertama dari daftar kursi yang sudah terurut A1.

<img width="300" height="775" alt="Screenshot 2026-05-25 211021" src="https://github.com/user-attachments/assets/865cf5e4-9e1b-4528-8af5-21212879aea7" /><br><br>
Lalu saya memilih menu 6. Kursi Terakhir. Program menampilkan kursi terakhir dari daftar kursi yang sudah terurut yaitu G8.
Setelah itu, saya memilih menu 2. Cari Kursi untuk mengecek status kursi.  
Kursi yang dicari adalah:  
- A1
- A2  
Karena kedua kursi tersebut sudah pernah dipesan, program menampilkan bahwa kursi sudah terisi.  

<img width="284" height="495" alt="Screenshot 2026-05-25 211049" src="https://github.com/user-attachments/assets/f197fb5c-100f-4191-9a28-dc1c8e8a69e6" /><br><br>
Lalu saya memilih menu 2. Cari Kursi untuk mencari kursi A3. Lalu program menampilkan Kursi A3 masih kosong. Lalu saya memilih menu 7. Keluar dan program menampilkan Program selesai.  


## Link Video Presentasi YouTube
https://youtu.be/YQ8EjVkStic
