harga_barang = int(input())
uang_dibayar = int(input())

if harga_barang >= uang_dibayar:
    print("uang tidak cukup")
    exit()

kembalian = uang_dibayar - harga_barang
nominal = [100000, 50000, 20000, 10000, 5000, 2000, 1000 ]

for i in nominal:
    jumlah = kembalian // i
    kembalian -= jumlah * i 
    print(f"{jumlah} uang sejumlah Rp.{i}")