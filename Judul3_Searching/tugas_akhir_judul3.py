def interpolation_search(data, n, target):
    low = 0
    high = n - 1

    while target >= data[low] and target <= data[high] and low <= high:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            break

        pos = low + int(((target - data[low]) / (data[high] - data[low])) * (high - low))
        print(f"Posisi estimasi: {pos}, NPM: {data[pos]}")

        if target > data[pos]:
            low = pos + 1
        elif target < data[pos]:
            high = pos - 1
        else:
            return pos

    if low < n and data[low] == target:
        return low
    return -1


def main():
    data = [2515061005, 2515061013, 2515061022, 2515061050, 2515061067, 2515061080, 2515061099]
    n = len(data)
    print(f"Daftar NPM Mahasiswa TI: {data}")

    while True:
        try:
            target = int(input("Masukkan NPM yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, masukkan angka!")
          
    pos = interpolation_search(data, n, target)
    if pos != -1:
        print(f"NPM {target} ditemukan pada indeks ke-{pos}")
    else:
        print(f"NPM {target} tidak ditemukan")


if __name__ == "__main__":
    main()
