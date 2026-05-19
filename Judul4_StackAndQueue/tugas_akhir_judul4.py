class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, kendaraan):
        if self.is_full():
            print("Antrian SPBU penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = kendaraan
        print(f"Kendaraan {kendaraan} masuk Antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian SPBU kosong")
            return
        print(f"Kendaraan {self.q[self.front_idx]} selesai mengisi BBM")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrian SPBU kosong")
            return
        print(f"Kendaraan paling depan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian SPBU kosong")
            return
        print("\nDaftar Antrian kendaraan:")
        i = self.front_idx

        while True:
            print("-", self.q[i])
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN


def main():
    SPBU = QueueArray()

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTRIAN SPBU ===")
        print("1. Kendaraan Masuk")
        print("2. Kendaraan Selesai")
        print("3. Lihat Antrian Depan")
        print("4. Tampilkan Semua Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue
        if pilih == 1:
            kendaraan = input("Masukkan nama/plat kendaraan: ")
            SPBU.enqueue(kendaraan)
        elif pilih == 2:
            SPBU.dequeue()
        elif pilih == 3:
            SPBU.peek()
        elif pilih == 4:
            SPBU.display()
        elif pilih == 5:
            print("Program selesai")
        else:
            print("Menu tidak valid")

if __name__ == "__main__":
    main()
