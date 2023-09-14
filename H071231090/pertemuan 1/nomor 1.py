print("Menghitung luas permukaan dan keliling segitiga")
X = float(input("Panjang sisi X: "))
Y = float(input("Panjang sisi Y: "))

Z = (X ** 2 + Y ** 2) ** 0.5

luas = 1/2*Y*X
keliling = X + Y + Z

print(f"Luas permukaan : {luas:.2}")
print(f"Keliling : {keliling:.2}")