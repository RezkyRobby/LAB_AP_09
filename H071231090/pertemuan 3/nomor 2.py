total_harga = int(input("Masukkan total harga: "))
jumlah_uang = int(input("Masukkan jumlah uang yang diberikan: "))

denominasi_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200]

kembalian = jumlah_uang - total_harga

if kembalian < 0:
    print("Jumlah uang yang diberikan kurang.")
else:
    print("Kembalian: {} rupiah".format(kembalian))

for uang in denominasi_uang:
    jumlah_lembar = kembalian // uang
    kembalian %= uang
    print("{} uang sejumlah Rp.{}".format(jumlah_lembar, uang))
   
