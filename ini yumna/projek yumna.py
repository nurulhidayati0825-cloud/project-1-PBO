class Member:
    def __init__(self, nama):
        self.nama = nama
        self.poin = 0

    def tambah_poin(self, total):
        if total >= 150000:
            self.poin += (total // 150000) * 1000
        elif total >= 100000:
            self.poin += 1000
        elif total >= 50000:
            self.poin += 750
        elif total >= 30000:
            self.poin += 250

    def hitung_diskon(self, total):
        return int((self.poin // 5000) * 0.25 * total)


# Program
nama = input("Nama member: ")
m = Member(nama)

while True:
    total = int(input("\nTotal belanja (0 untuk keluar): "))
    if total == 0:
        break

    diskon = m.hitung_diskon(total)
    bayar = total - diskon

    print("Diskon :", diskon)
    print("Bayar  :", bayar)

    m.tambah_poin(total)
    print("Poin sekarang:", m.poin)