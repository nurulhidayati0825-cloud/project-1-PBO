class Ruang:
    def __init__(self, kode, nama, kapasitas):
        self.kode = kode
        self.nama = nama
        self.kapasitas = kapasitas

    def tampilkan_data(self):
        print("=== Data Ruang ===")
        print("Kode      :", self.kode)
        print("Nama      :", self.nama)
        print("Kapasitas :", self.kapasitas)
        print()