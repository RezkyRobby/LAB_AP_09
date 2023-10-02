def kucing_tikus(k1, k2, t):
    jarak_k1 = abs(k1-t)
    jarak_k2 = abs(k2-t)
    if jarak_k1 == jarak_k2:
        return 'Mouse C'
    elif jarak_k1 > jarak_k2:
        return 'Cat B'
    else:
        return 'Cat A'


print('Masukkan Jarak Kucing A,B dan Tikus C')
try:
    jarak_Kucing1 = int(input('Cat A = '))
    jarak_Kucing2 = int(input('Cat B = '))
    jarak_tikus = int(input('Mos C = '))
    print(
        f'Cat and Mouse(Cat A = {jarak_Kucing1}, Cat B = {jarak_Kucing2}, Mouse C = {jarak_tikus})')
    print(kucing_tikus(jarak_Kucing1, jarak_Kucing2, jarak_tikus))
except ValueError as pesan:
    print('Terjadi Kesalahan =', pesan)
