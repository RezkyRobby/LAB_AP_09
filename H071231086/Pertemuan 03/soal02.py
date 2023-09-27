# Input harga barang dan nilai uang yang dibayarkan
harga_barang = int(input())
uang_dibayarkan = int(input())

# Menghitung kembalian
kembalian = uang_dibayarkan - harga_barang

# Daftar pecahan uang yang tersedia
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Menampilkan hasil kembalian
for pecahan in pecahan_uang:
    jumlah_pecahan = kembalian // pecahan
    if jumlah_pecahan > 0:
        print(f"{jumlah_pecahan} uang sejumlah Rp.{pecahan}")
        kembalian %= pecahan
    else:
        print(f"0 uang sejumlah Rp.{pecahan}")




