harga = int(input())
uang = int(input())
kembalian = uang - harga
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if harga > uang :
    print("uang tidak cukup")
    exit()
for pecahan in pecahan_uang:
    jumlah = kembalian // pecahan
    print(f'{jumlah} uang sejumlah Rp.{pecahan}')
    kembalian -= jumlah * pecahan
