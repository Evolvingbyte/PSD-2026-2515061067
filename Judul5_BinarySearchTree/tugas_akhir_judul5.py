class Node:
    def __init__(self, nomor_kursi):
        self.nomor_kursi = nomor_kursi
        self.left = None
        self.right = None

class BioskopBST:
    def __init__(self):
        self.root = None
    # Insert kursi
    def insert_node(self, root, nomor_kursi):
        if root is None:
            return Node(nomor_kursi)
        if nomor_kursi < root.nomor_kursi:
            root.left = self.insert_node(root.left, nomor_kursi)
        elif nomor_kursi > root.nomor_kursi:
            root.right = self.insert_node(root.right, nomor_kursi)
        else:
            print("Kursi sudah dipesan!")
        return root

    def pesan_kursi(self, nomor_kursi):
        self.root = self.insert_node(self.root, nomor_kursi)

    def search_node(self, root, nomor_kursi):
        if root is None:
            return False
        if root.nomor_kursi == nomor_kursi:
            return True
        if nomor_kursi < root.nomor_kursi:
            return self.search_node(root.left, nomor_kursi)
        return self.search_node(root.right, nomor_kursi)

    def cari_kursi(self, nomor_kursi):
        return self.search_node(self.root, nomor_kursi)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.nomor_kursi, end=" ")
        self.inorder(root.right)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.nomor_kursi

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.nomor_kursi


def main():
    bioskop = BioskopBST()
    pilih = 0

    while pilih != 7:
        print("\n=== SISTEM KURSI BIOSKOP ===")
        print("1. Pesan Kursi")
        print("2. Cari Kursi")
        print("3. Tampilkan Kursi Terurut")
        print("4. Jumlah Kursi Terisi")
        print("5. Kursi Pertama")
        print("6. Kursi Terakhir")
        print("7. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            kursi = input("Masukkan nomor kursi: ").upper()
            if bioskop.cari_kursi(kursi):
                print("Kursi sudah dipesan!")
            else:
                bioskop.pesan_kursi(kursi)
                print(f"Kursi {kursi} berhasil dipesan.")
        elif pilih == 2:
            kursi = input("Cari nomor kursi: ").upper()
            if bioskop.cari_kursi(kursi):
                print(f"Kursi {kursi} sudah terisi.")
            else:
                print(f"Kursi {kursi} masih kosong.")
        elif pilih == 3:
            print("Daftar kursi terurut: ", end="")
            bioskop.inorder(bioskop.root)
            print()
        elif pilih == 4:
            print(f"Jumlah kursi terisi: {bioskop.count_nodes(bioskop.root)}")
        elif pilih == 5:
            print(f"Kursi pertama: {bioskop.find_min(bioskop.root)}")
        elif pilih == 6:
            print(f"Kursi terakhir: {bioskop.find_max(bioskop.root)}")
        elif pilih == 7:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
