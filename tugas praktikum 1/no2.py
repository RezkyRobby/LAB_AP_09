print("Konversi suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")

celcius = float(input("Masukkan suhu dalam Celcius: "))

kelvin = float(celcius + 273.15)
reamur = float(4/5 * celcius)
fahrenheit = float((celcius * 9/5) + 32)

print(f"hasil konversi dari suhu {celcius} derajat celcius ke Kelvin adalah : {kelvin}K")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke Reamur adalah : {reamur}R")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke Fahrenheit adalah : {fahrenheit}F")