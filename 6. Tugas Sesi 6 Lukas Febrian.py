#input
l = input("Umur kurang dari 2 Tahun:")
m = input("Umur kurang dari 4 Tahun + Jika tinggi anak 2-3 Tahun melebihi 70 cm:")
o = input("Umur kurang dari 7 Tahun + Jika tinggi anak 4-6 Tahun melebihi 120 cm:")
q = input("Umur kurang dari 10 Tahun + Jika tinggi anak 8-9 Tahun melebihi 150 cm:")
s = input("Umur lebih dari 10 Tahun:")
kdjur = input("Masukan Kode Jurusan [Empat Tahun|Tujuh Tahun|Sepuluh Tahun] ")
jml = input("Masukan Jumlah Harga Dari Setiap Umur")

#proses
if kdjur=="Empat Tahun":
    Umur="4 Tahun"
    Harga=30000
elif kdjur=="Empat Tahun":
    Umur="7 Tahun"
    Harga=40000
else:
    Umur="Sepuluh Tahun"
    Harga=50000

#output
print("__________________________________________")
print('PENJUALAN TIKET WAHANA, DASAR PEMOGRAMAN')
print("__________________________________________")
print("Umur kurang dari 2 Tahun: Dilarang Masuk")
print("Umur kurang dari 4 Tahun + Jika tinggi anak 2-3 Tahun melebihi 70 cm: 40.000")
print("Umur kurang dari 7 Tahun + Jika tinggi anak 4-6 Tahun melebihi 120 cm: 55.000")
print("Umur kurang dari 10 Tahun + Jika tinggi anak 8-9 Tahun melebihi 120 cm: 70.000")
print("Umur lebih dari 10 Tahun: 80.000")
print("_____________________________________________")
print("Hasil Akhir Adalah 245.000")
print("_____________________________________________")