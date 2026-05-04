from pemilik import Pemilik
from dokter import Dokter
from ruang import Ruang
from pemeriksaan import Pemeriksaan
from hewan import Hewan

def main():
    pemilik1 = Pemilik("Khalifah Ayu", "Surakarta", "082145678901")
    hewan1 = Hewan("Mochi", "Kucing", 2, "Demam dan tidak nafsu makan")
    dokter1 = Dokter("Dr. Salsabila", "D002", "Hewan Kecil", 120000)
    ruang1 = Ruang("R02", "Ruang Kucing", 4)

    pemilik1.tambah_hewan(hewan1)

    print("\n[TEST SKENARIO 1: RAWAT JALAN]")
    periksa1 = Pemeriksaan(hewan1, dokter1)
    periksa1.tampilkan_detail()

    print("\n[TEST SKENARIO 2: RAWAT INAP]")
    periksa2 = Pemeriksaan(hewan1, dokter1, ruang1, 3)
    periksa2.tampilkan_detail()

    print("\n[DATA MASTER]")
    pemilik1.tampilkan_data()
    hewan1.tampilkan_info()
    dokter1.tampilkan_data()
    ruang1.tampilkan_data()

if __name__ == "__main__":
    main()