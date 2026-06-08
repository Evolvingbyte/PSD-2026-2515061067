class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.nomor_polisi = None
        self.nomor_tiket = None
        self.state = SlotState.EMPTY


class SistemParkir:
    def __init__(self, jumlah_slot=10):
        self.jumlah_slot = jumlah_slot
        self.table = [Entry() for _ in range(jumlah_slot)]

    def hash_function(self, nomor_tiket):
        return nomor_tiket % self.jumlah_slot

    def parkir_masuk(self, nomor_tiket, nomor_polisi):
        index = self.hash_function(nomor_tiket)

        for step in range(self.jumlah_slot):
            i = (index + step) % self.jumlah_slot
            if self.table[i].state in (SlotState.EMPTY, SlotState.DELETED):
                self.table[i].nomor_tiket = nomor_tiket
                self.table[i].nomor_polisi = nomor_polisi
                self.table[i].state = SlotState.OCCUPIED
                print(f"Kendaraan {nomor_polisi} parkir di slot {i}")
                return True
        print("Parkiran penuh!")
        return False

    def cari_kendaraan(self, nomor_tiket):
        index = self.hash_function(nomor_tiket)
        for step in range(self.jumlah_slot):
            i = (index + step) % self.jumlah_slot
            if self.table[i].state == SlotState.EMPTY:
                return None
            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].nomor_tiket == nomor_tiket):
                return i
        return None

    def kendaraan_keluar(self, nomor_tiket):
        slot = self.cari_kendaraan(nomor_tiket)
        if slot is not None:
            print(f"Kendaraan {self.table[slot].nomor_polisi} keluar dari slot {slot}")
            self.table[slot].state = SlotState.DELETED
            return True
        print("Kendaraan tidak ditemukan")
        return False

    def tampilkan_parkiran(self):
        print("\n=== STATUS PARKIRAN ===")
        for i in range(self.jumlah_slot):
            print(f"Slot {i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("Kosong")
            elif self.table[i].state == SlotState.DELETED:
                print("Pernah Terisi")
            else:
                print(
                    f"{self.table[i].nomor_polisi} "
                    f"(Tiket {self.table[i].nomor_tiket})"
                )


def main():
    parkir = SistemParkir(10)

    parkir.parkir_masuk(1, "BE1234AA")
    parkir.parkir_masuk(11, "BE5678BB")
    parkir.parkir_masuk(21, "BE9012CC")
    parkir.parkir_masuk(2, "BE3456DD")
    parkir.tampilkan_parkiran()
    print("\nMencari tiket nomor 11...")
    slot = parkir.cari_kendaraan(11)

    if slot is not None:
        print(f"Kendaraan ditemukan di slot {slot}")
    else:
        print("Kendaraan tidak ditemukan")
    print("\nKendaraan keluar:")
    parkir.kendaraan_keluar(11)
    parkir.tampilkan_parkiran()

if __name__ == "__main__":
    main()
