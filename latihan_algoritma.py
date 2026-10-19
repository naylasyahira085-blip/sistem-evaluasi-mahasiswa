#Latihan algoritma

#input nilai mahasiswa
tugas = float(input("Masukan nilai tugas:"))
uts = float(input("Masukan nilai uts:"))
uas = float(input("Masukan nilai uas:"))
kehadiran = float(input("Masukan persentase kehadiran:"))

#Menghitung nilai akhir
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

#Menampilkan nilai akhir
print("nilai akhir:", nilai_akhir)

#Menentukan status kelulusan
if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
        print("status:LULUS DENGAN PREDIKAT")
    else:
        print("status :LULUS")
else:
    print("status:BELUM LULUS")
