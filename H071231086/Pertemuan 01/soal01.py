
print('Menghitung luas permukaan dan keliling segitiga')
a = float(input('Panjang Y =') )  
t = float(input('Panjang X ='))
m = (t**2 + a**2)

luas = a*t*(1/2)
keliling = a+t+m
print(f'Luas permukaan = {luas:.3f}')
print(f'Keliling = {keliling:.3f}')