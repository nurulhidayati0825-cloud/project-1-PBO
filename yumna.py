from pemilik import Pemilik
from dokter import Dokter
from ruang import Ruang
from pemeriksaan import Pemeriksaan
from hewan import Hewan

def main():
    # 1. Inisialisasi Objek
    pemilik1 = Pemilik("owi", "solo", "08123456789")
    hewan1 = Hewan("prenjak", "burung", 2, "Sakit")
    dokter1 = Dokter("Dr. owo", "Y001", "unggas", 50000)
    ruang1 = Ruang("R01", "Ruang burung", 0)

    # 2. Relasi Pemilik dan Hewan
    pemilik1.tambah_hewan(hewan1)

    # 3. Testing Skenario 1: Pemeriksaan TANPA rawat inap
    print("\n[TEST SKENARIO 1: RAWAT JALAN")
    periksa1 = Pemeriksaan(hewan1, dokter1,ruang1, 0)
    periksa1.tampilkan_detail()

    # 4. Testing Skenario 2: Pemeriksaan DENGAN rawat inap
    print("\n[TEST SKENARIO 2: RAWAT INAP]")
    periksa2 = Pemeriksaan(hewan1, dokter1, ruang1, 5)
    periksa2.tampilkan_detail()

    # 5. Menampilkan Data Master
    print("\n[DATA MASTER]")
    pemilik1.tampilkan_data()
    hewan1.tampilkan_info()
    dokter1.tampilkan_data()
    ruang1.tampilkan_data()

if __name__ == "__main__":
    main()