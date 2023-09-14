print("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")
Celcius = float(input("Masukkan Suhu dalam Celcius: "))

Kelvin = 273 + Celcius
Reamur = 4/5 * Celcius
Fahrenheit = (Celcius * 9/5) + 32

print(f"Hasil konversi dari suhu {Celcius:.0f} derajat Celcius ke Kelvin adalah  : {Kelvin:.0f}K")
print(f"Hasil konversi dari suhu {Celcius:.0f} derajat Celcius ke Reamur adalah : {Reamur:.0f}R")
print(f"Hasil konversi dari suhu {Celcius:.0f} derajat Celcius ke Fahrenheit adalah : {Fahrenheit:.0f}F")