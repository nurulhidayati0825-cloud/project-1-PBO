class Dokter:
    def __init__(self, nama, id_dokter, spesialisasi, tarif):
        self.nama = nama
        self.id_dokter = id_dokter
        self.spesialisasi = spesialisasi
        self.tarif = tarif

    def tampilkan_data(self):
        print("=== Data Dokter ===")
        print("Nama         :", self.nama)
        print("ID Dokter    :", self.id_dokter)
        print("Spesialisasi :", self.spesialisasi)
        print("Tarif        : Rp", self.tarif)
        print()