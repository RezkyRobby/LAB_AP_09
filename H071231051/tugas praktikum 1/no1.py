import math

print("Menghitung luas permukaan dan keliling segitiga")

x = float(input("panjang sisi x: "))
y = float(input("panjang sisi y: "))

z = math.sqrt(x**2 + y**2)

keliling = x + y + z
luas =  1/2 * x * y 

print(f"Luas Permukaan : {luas:.2f}")
print(f"Keliling: {keliling:.2f}")