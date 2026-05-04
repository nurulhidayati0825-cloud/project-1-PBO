class Pemeriksaan:
    def __init__(self, hewan, dokter, ruang=None, lama_inap=0):
        self.hewan = hewan
        self.dokter = dokter
        self.ruang = ruang
        self.lama_inap = lama_inap

    def hitung_biaya(self):
        biaya = self.dokter.tarif
        if self.lama_inap > 0:
            biaya += 200000 * self.lama_inap
        return biaya

    def tampilkan_detail(self):
        print("=== Detail Pemeriksaan ===")
        print("Hewan  :", self.hewan.nama)
        print("Dokter :", self.dokter.nama)

        if self.ruang:
            print("Ruang  :", self.ruang.nama)
            print("Lama Inap :", self.lama_inap, "hari")
        else:
            print("Tanpa Rawat Inap")

        print("Total Biaya : Rp", self.hitung_biaya())
        print()