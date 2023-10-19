print('Konversi Suhu dari celcius ke Kelvin, Reamur dan Fahrenheit')

x=input('Masukkan suhu dalam Celcius : ') #Nilai Celcius
x=float(x) 

kelvin=int(x+273.15) #Menghitung suhu dalam Kelvin

reamur=int(x*4/5) #Menghitung suhu dalam Reamur

fahrenheit=int((x*9/5)+32) #Menghitung suhu dalam Fahrenheit

print('Hasil konversi dari suhu',x,'derajat celcius ke Kelvin adalah :',kelvin,'K')
print('Hasil konversi dari suhu',x,'derajat celcius ke Reamur adalah :',reamur,'R')
print('Hasil konversi dari suhu',x,'derajat celcius ke Fahrenheit adalah :',fahrenheit,'F')
