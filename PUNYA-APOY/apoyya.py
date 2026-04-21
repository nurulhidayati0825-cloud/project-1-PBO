# Contoh sederhana OOP di Python

class Kendaraan:
    # Constructor
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    # Method
    def tampilkan_info(self):
        print(f"Nama kendaraan : {self.nama}")
        print(f"Warna          : {self.warna}")

    def jalan(self):
        print(f"{self.nama} sedang berjalan.")


# Pewarisan / Inheritance
class Mobil(Kendaraan):
    def __init__(self, nama, warna, jumlah_pintu):
        super().__init__(nama, warna)
        self.jumlah_pintu = jumlah_pintu

    def tampilkan_info(self):
        print("=== Data Mobil ===")
        print(f"Nama kendaraan : {self.nama}")
        print(f"Warna          : {self.warna}")
        print(f"Jumlah pintu   : {self.jumlah_pintu}")

    def klakson(self):
        print(f"{self.nama} berbunyi: Tin tin!")


# Membuat objek
kendaraan1 = Kendaraan("Sepeda Motor", "Hitam")
mobil1 = Mobil("Toyota Avanza", "Putih", 4)

# Menjalankan method
kendaraan1.tampilkan_info()
kendaraan1.jalan()

print()  # spasi

mobil1.tampilkan_info()
mobil1.jalan()
mobil1.klakson()