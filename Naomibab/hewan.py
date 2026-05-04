class Hewan:
    def __init__(self, nama, jenis, umur, kondisi):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.kondisi = kondisi

    def tampilkan_info(self):
        print("=== Data Hewan ===")
        print("Nama    :", self.nama)
        print("Jenis   :", self.jenis)
        print("Umur    :", self.umur, "tahun")
        print("Kondisi :", self.kondisi)
        print()