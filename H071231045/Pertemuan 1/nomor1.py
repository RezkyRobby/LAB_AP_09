print('Menghitung Luas Permukaan Dan Keliling Segitiga')

x = float(input('Masukkan nilai x   : '))
y = float(input('Masukkan nilai y   : '))

luas = 1/2*(x*y)
z = (x**2+y**2)**0.5
keliling = x+y+z

print(F'Luas permukaan :{luas: .2f}')
print(f'keliling       :{keliling: .2f}')  