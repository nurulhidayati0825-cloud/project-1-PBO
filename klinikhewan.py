# Superclass 
class Hewan:
    def __init__(self, nama, usia, berat, pemilik):
        self.nama = nama
        self.usia = usia
        self.berat = berat
        self.pemilik = pemilik

    def tampil_info(self):
        print("Nama Hewan :", self.nama)
        print("Usia :", self.usia)
        print("Berat :", self.berat)
        print("Pemilik :", self.pemilik)

    def hitung_biaya(self):
        return 0


# Subclass Kucing
class Kucing(Hewan):
    def hitung_biaya(self):
        return 150000


# Subclass Anjing
class Anjing(Hewan):
    def hitung_biaya(self):
        return 200000


# Kucing Persia
class KucingPersia(Kucing):
    def hitung_biaya(self):
        return 300000


# Kucing Kampung
class KucingKampung(Kucing):
    def hitung_biaya(self):
        return 100000


# Anjing Penjaga
class AnjingPenjaga(Anjing):
    def hitung_biaya(self):
        return 400000


# Anjing Rumahan
class AnjingRumahan(Anjing):
    def hitung_biaya(self):
        return 250000


# Superclass Tenaga Layanan
class TenagaLayanan:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def tampil_pegawai(self):
        print("Nama Pegawai :", self.nama)
        print("Nomor Pegawai :", self.nomor)


# Dokter Hewan
class DokterHewan(TenagaLayanan):
    pass


# Perawat Hewan
class PerawatHewan(TenagaLayanan):
    pass


# Program utama
kucing1 = KucingPersia("naba", 2, 4.5, "Nao")
anjing1 = AnjingPenjaga("bana", 3, 10, "Ruba")

dokter1 = DokterHewan("Dr. Sinta", "D001")
perawat1 = PerawatHewan("Rina", "P001")

print("=== DATA HEWAN ===")
kucing1.tampil_info()
print("Biaya :", kucing1.hitung_biaya())

print()

anjing1.tampil_info()
print("Biaya :", anjing1.hitung_biaya())

print("\n=== DATA PEGAWAI ===")
dokter1.tampil_pegawai()

print()

perawat1.tampil_pegawai()