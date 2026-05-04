class Pemilik:
    def __init__(self, nama, alamat, no_hp):
        self.nama = nama
        self.alamat = alamat
        self.no_hp = no_hp
        self.daftar_hewan = []

    def tambah_hewan(self, hewan):
        self.daftar_hewan.append(hewan)

    def tampilkan_data(self):
        print("=== Data Pemilik ===")
        print("Nama   :", self.nama)
        print("Alamat :", self.alamat)
        print("No HP  :", self.no_hp)
        print()