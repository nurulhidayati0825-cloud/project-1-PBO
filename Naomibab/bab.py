class RekeningBank:
    """Kelas untuk merepresentasikan rekening bank sederhana."""

    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.saldo = saldo_awal

    def setor(self, jumlah):
        """Metode untuk menambah saldo."""
        if jumlah > 0:
            self.saldo += jumlah
            print(f"✅ Berhasil setor Rp{jumlah}. Saldo saat ini: Rp{self.saldo}")
        else:
            print("❌ Jumlah setor harus lebih dari 0.")

    def tarik(self, jumlah):
        """Metode untuk mengambil uang."""
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"💸 Berhasil tarik Rp{jumlah}. Sisa saldo: Rp{self.saldo}")
        elif jumlah > self.saldo:
            print("❌ Saldo tidak cukup!")
        else:
            print("❌ Jumlah tarik tidak valid.")

    def cek_info(self):
        """Metode untuk menampilkan informasi akun."""
        print(f"\n--- Info Rekening ---")
        print(f"Pemilik: {self.pemilik}")
        print(f"Total Saldo: Rp{self.saldo}")
        print(f"---------------------\n")

nasabah1 = RekeningBank("Andi", 500000)

nasabah1.cek_info()
nasabah1.setor(200000)
nasabah1.tarik(100000)
nasabah1.cek_info()