class Member:
    def __init__(self, nama, id_member, biaya_dasar):
        self.nama = nama
        self.id_member = id_member
        self.biaya_dasar = biaya_dasar

    def tampilkan_info(self):
        print(f"ID: {self.id_member} | Nama: {self.nama}")

    def hitung_tagihan(self):
        # Default hanya biaya dasar
        return self.biaya_dasar

class MemberVIP(Member):
    def __init__(self, nama, id_member, biaya_dasar, biaya_fasilitas):
        super().__init__(nama, id_member, biaya_dasar)
        self.biaya_fasilitas = biaya_fasilitas

    def hitung_tagihan(self):
        # Override: Biaya Dasar + Biaya Fasilitas Tambahan
        return self.biaya_dasar + self.biaya_fasilitas

class MemberPelajar(Member):
    def __init__(self, nama, id_member, biaya_dasar, diskon):
        super().__init__(nama, id_member, biaya_dasar)
        self.diskon = diskon

    def hitung_tagihan(self):
        # Override: Biaya Dasar dikurangi Diskon Pelajar
        return self.biaya_dasar - (self.biaya_dasar * self.diskon)

#MemberReguler
m1 = Member("Andi", "REG01", 300000)
#MemberVIP (Ada tambahan biaya fasilitas 150rb)
m2 = MemberVIP("Budi", "VIP01", 300000, 150000)
#MemberPelajar (Diskon 20% atau 0.2)
m3 = MemberPelajar("Cici", "STU01", 300000, 0.2)

daftar_member = [m1, m2, m3]

print("--- LAPORAN TAGIHAN BULANAN ---")
for m in daftar_member:
    m.tampilkan_info()
    print(f"Total Tagihan: Rp {m.hitung_tagihan():,}")
    print("-" * 30)