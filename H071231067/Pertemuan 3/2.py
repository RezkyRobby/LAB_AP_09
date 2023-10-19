while True:
    harga=int(input('Harga Barang = '))
    uang=int(input('Uang = '))
    kembalian=uang - harga
    if kembalian>0:break
    else:print('Uang Tidak Cukup')

jumlah=[0,0,0,0,0,0,0]
uang=[100000,50000,20000,10000,5000,2000,1000]

for i in range(len(jumlah)):
    if kembalian>=uang[i]:
        jumlah[i]=kembalian//uang[i]
        kembalian=kembalian%uang[i]
    
for i in range(len(jumlah)):
    print(f'{jumlah[i]} Uang sejumlah Rp.{uang[i]}')