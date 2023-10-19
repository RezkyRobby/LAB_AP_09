x=int(input('Masukkan Nilai = '))
urutan_fib=[0,1]
    
while len(urutan_fib)<x:
        angka_selanjutnya=urutan_fib[-1]+urutan_fib[-2]
        urutan_fib.append(angka_selanjutnya)

if x<=0:print('Tidak Valid')
elif x==1:print('0')
else:
 for angka in urutan_fib:
        print(angka,end=' ')