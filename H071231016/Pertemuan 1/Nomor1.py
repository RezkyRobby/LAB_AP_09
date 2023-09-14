#Menentukan luas dan keliling segitiga
print ("Menghitung luas dan kelliling segitiga")
a = float (input('masukkan nilai alas segitiga:'))
t = float (input('masukkan nilai tinggi segitiga:'))

luas = (a*t)/2 
m = (a**2+t**2)*0.5 #pakai phytagoras
keliling = a + t + m

print(f'luas permukaan:{luas: .2f}')
print(f'keliling : {keliling: .2f}')
