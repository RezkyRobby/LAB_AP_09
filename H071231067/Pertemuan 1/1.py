print('Menghitung Luas Permukaan dan Keliling Segitiga')

x=input('Panjang Sisi X : ')
x=float(x)

y=input('Panjang Sisi Y : ')
y=float(y)

z=((x**2)+(y**2))**0.5 #rumus mencari sisi miring segitiga

luas=0.5*y*x #rumus mencari luas segitiga

keliling=x+y+z #rumus mencari keliling segitiga)

print('Luas Permukaan : ',format(luas,'.2f'))
print('Keliling : ',format(keliling,'.2f'))