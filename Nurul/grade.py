# fungsi hitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai_akhir
    
# fungsi kategori nilai
def tentukan_kategori(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    else:
        return "D"

# fungsi tampilkan hasil
def tampilkan_hasil(nama, nilai_akhir, kategori):
    print("=== HASIL PENILAIAN ===")
    print("Nama Mahasiswa : ", nama)
    print("Nilai Akhir:", round(nilai_akhir, 2))
    print("Kategori       :", kategori)
    print("========================")
        
# main program
print("=== PROGRAM PENGHITUNG NILAI AKHIR ===")
nama = input("Masukkan nama: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai uts: "))
uas = float(input("Masukkan nilai uas: "))

nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
kategori = tentukan_kategori(nilai_akhir)
tampilkan_hasil(nama, nilai_akhir, kategori)
