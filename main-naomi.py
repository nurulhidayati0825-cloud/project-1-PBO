from hewan import Hewan
from pemilik import Pemilik
from dokter import Dokter
from ruang import Ruang
from pemeriksaan import Pemeriksaan

def main():
    pemilik1 = Pemilik("Nomi", "Jateng", "0857272749146")
    hewan1 = Hewan("Mimi", "Kucing", 3, "Patah Kaki")
    dokter1 = Dokter("Dr. Apoy", "D017", "Mamalia", 350000)
    ruang1 = Ruang("R10", "Ruang Mamalia", 1)

    pemilik1.tambah_hewan(hewan1)

    print("\n[TEST SKENARIO 1: RAWAT JALAN]")
    periksa1 = Pemeriksaan(hewan1, dokter1)
    periksa1.tampilkan_detail()

    print("\n[TEST SKENARIO 2: RAWAT INAP]")
    periksa2 = Pemeriksaan(hewan1, dokter1, ruang1, 2)
    periksa2.tampilkan_detail()

    print("\n[DATA MASTER]")
    pemilik1.tampilkan_data()
    hewan1.tampilkan_info()
    dokter1.tampilkan_data()
    ruang1.tampilkan_data()

if __name__ == "__main__":
    main()
