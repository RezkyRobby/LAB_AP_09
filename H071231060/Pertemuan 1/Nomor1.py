x = float(input("masukkan nilai x="))
y = float(input("masukkan nilai y="))

z = ((x*x + y*y)**0.5)

Luas = ((1/2)*x*y)
luasFixed = format(Luas, ".2f")
print("Luas Segitiga =",luasFixed)
Keliling = x+y+z
KelilingFixed = format(Keliling, ".2f")
print("Keliling Segitiga =",KelilingFixed)