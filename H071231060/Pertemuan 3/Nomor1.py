# Soal 1 : Menghasilkan Jumlah Suku Fibonacci
suku = int(input("masukkan bilangan positif:"))
n1 = 0
n2 = 1
s = 0

if suku > 0 :
    while suku > s:
        print(n1, end=" ")
        Un = n1 + n2
        n1 = n2 
        n2 = Un
        s += 1        
elif suku == 1:
    print(n1)
else:
    print('Input Bilangan harus Positif')


