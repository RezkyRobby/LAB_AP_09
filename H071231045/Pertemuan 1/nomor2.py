print('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')

a = int(input('Masukkan Suhu dalam Celsius : '))

kelvin = int(a+273)
reamur = int(4/5*a)
fahrenheit = int((9/5*a)+32)

print(f'Hasil konversi dari suhu {a} derajat celcius ke kelvin adalah      :{kelvin: }K')
print(f'Hasil konversi dari suhu {a} derajat celcius ke Reamur adalah      :{reamur: }R')
print(f'Hasil konversi dari suhu {a} derajat celcius ke Fahrenheit adalah  :{fahrenheit: }F')