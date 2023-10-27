print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
c = int(input('Masukkan Suhu dalam Celcius = '))
f = (9/5)*c+32
k = c+273.15
r = (4/5)*c
print(f'Hasil konversi dari suhu {c} derajat celcius ke Kelvin adalah = {k}K')
print(f'Hasil konversi dari suhu {c} derajat celcius ke Reamur adalah = {r}R')
print(f'Hasil konversi dari suhu {c} derajat celcius ke Fahrenheit adalah = {f}F')
