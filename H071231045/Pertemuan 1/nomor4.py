print('Pengujian jenis karakter')
karakter = input('Masukkan sebuah karakter: ')

Hurufkapital = 'A' <= karakter <= 'Z' # a >= 'A' and a <= 'Z' 
Hurufkecil = 'a' <= karakter <= 'z'  # a >= 'a' and a <= 'z'
Angka = '0' <= karakter <= '9'  # a >= '0' and a <= '9' 

print(f'Huruf kapital? {Hurufkapital}')
print(f'Huruf kecil? {Hurufkecil}')
print(f'Angka? {Angka}')
