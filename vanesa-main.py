from pemilik import Pemilik
from dokter import Dokter
from ruang import Ruang
from pemeriksaan import Pemeriksaan
from hewan import Hewan

def main():
    # 1. Inisialisasi Objek
    pemilik1 = Pemilik("Haechan", "Bandung", "087765432100")
    hewan1 = Hewan("Chiko", "Gecko", 2, "Diare")
    dokter1 = Dokter("Dr. Jaemin", "D005", "Reptil dan Amphibi", 150000)
    ruang1 = Ruang("R05", "Ruang Perawatan Reptil", 8)

    # 2. Relasi Pemilik dan Hewan
    pemilik1.tambah_hewan(hewan1)

    # 3. Testing Skenario 1: Pemeriksaan TANPA rawat inap
    print("\n[TEST SKENARIO 1: RAWAT JALAN]")
    periksa1 = Pemeriksaan(hewan1, dokter1)
    periksa1.tampilkan_detail()
    
    # 4. Testing Skenario 2: Pemeriksaan DENGAN rawat inap
    print("\n[TEST SKENARIO 2: RAWAT INAP]")
    periksa2 = Pemeriksaan(hewan1, dokter1, ruang1, 4)
    periksa2.tampilkan_detail()

    # 5. Menampilkan Data Master
    print("\n[DATA MASTER]")
    pemilik1.tampilkan_data()
    hewan1.tampilkan_info()
    dokter1.tampilkan_data()
    ruang1.tampilkan_data()

if __name__ == "__main__":
    main()