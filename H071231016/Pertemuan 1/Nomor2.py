#Nomor2 Konversi suhu dari celcius ke kelvin,reamur dan fahreinheit
print('konversi suhu dari celcius ke kelvin,reamur, dan celcius')
c= int(input('Masukkan suhu dalam celcius:'))

K= int(c+273)
R= int((4/5)*c)
F= int(9/5*c)+32

print(f'Hasil Konversi dari {c} celcius ke kelvin adalah: {K}K')
print(f'Hail konversi dari {c} celcius ke Reamur adalah: {R}R')
print(f'Hasil konversi dari {c} celcius ke Fahreinheit adalahh: {F}F')