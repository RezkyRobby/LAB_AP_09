# Soal 2 : Menghitung Kembalian dari Suatu Transaksi
# harga = int(input('Harga Barang : '))
# bayar = int(input('Nilai Uang :  '))
# if bayar < harga:
#    print('Nilai Uang Kurang!')
#    exit()

# kembalian = bayar - harga

# Rp_100k = 0
# Rp_50k = 0
# Rp_20k = 0
# Rp_10k = 0
# Rp_5k = 0
# Rp_2k = 0
# Rp_1k = 0

# while kembalian > 0:
#    if kembalian >= 100000:
#       Rp_100k += 1
#       kembalian -= 100000
#    elif kembalian >= 50000:
#       Rp_50k += 1
#       kembalian -= 50000
#    elif kembalian >= 20000:
#       Rp_20k += 1
#       kembalian -= 20000
#    elif kembalian >= 10000:
#       Rp_10k += 1
#       kembalian -= 10000
#    elif kembalian >= 5000:
#       Rp_5k += 1
#       kembalian -= 5000
#    elif kembalian >= 2000:
#       Rp_2k += 1
#       kembalian -= 2000
#    elif kembalian >= 1000:
#       Rp_1k += 1
#       kembalian -= 1000

# print(f'{Rp_100k} uang sejumlah Rp.100000')
# print(f'{Rp_50k} uang sejumlah Rp.50000')
# print(f'{Rp_20k} uang sejumlah Rp.20000')
# print(f'{Rp_10k} uang sejumlah Rp.10000')
# print(f'{Rp_5k} uang sejumlah Rp.5000')
# print(f'{Rp_2k} uang sejumlah Rp.2000')
# print(f'{Rp_1k} uang sejumlah Rp.1000')

harga_barang = int(input("Masukkan harga barang ="))
jumlah_uang = int(input("masukkan jumlah uang anda ="))
kembalian = jumlah_uang-harga_barang
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if harga_barang>jumlah_uang:
    print("nilai barang lebih besar dari uang!")
    exit()
for i in pecahan_uang:
    sisa = kembalian//i
    if sisa >=0:
        kembalian -= sisa * i
        print(f"{sisa} uang sejumlah Rp.{i}")
