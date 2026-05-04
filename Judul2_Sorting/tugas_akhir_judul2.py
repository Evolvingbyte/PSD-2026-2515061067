def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort_harga(barang, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if barang[j]["harga"] > barang[j + 1]["harga"]:
                tukar(barang, j, j + 1)

def main():
    try:
        n = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Input tidak valid!")
        return

    barang = []
    

    print("\nMasukkan data barang Warung Madura:")
    for i in range(n):
        print(f"\nBarang ke-{i + 1}")
        nama = input("Nama barang: ")

        while True:
            try:
                harga = int(input("Harga barang: "))
                barang.append({
                    "nama": nama,
                    "harga": harga
                })
                break
            except ValueError:
                print("Input harga tidak valid, silakan masukkan angka!")

    print("\nDaftar barang sebelum diurutkan:")
    for item in barang:
        print(f"{item['nama']} - Rp{item['harga']}")

    bubble_sort_harga(barang, n)

    print("\nDaftar barang setelah diurutkan berdasarkan harga termurah:")
    for item in barang:
        print(f"{item['nama']} - Rp{item['harga']}")

    print("\nDaftar barang setelah diurutkan berdasarkan harga termahal:")
    for item in reversed(barang):
        print(f"{item['nama']} - Rp{item['harga']}")


if __name__ == "__main__":
        main()
