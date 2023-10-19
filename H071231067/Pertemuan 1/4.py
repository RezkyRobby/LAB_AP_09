print('Pengujian Jenis Karakter')
print('------------------------')

x=input('Karakter = ')
x=str(x)

Kapital= x>='A'and x<='Z' #untuk mengetahui apakah string itu kapital atau bukan
kecil= x>='a' and x<= 'z'#untuk mengetahui apakah string itu huruf kecil atau bukan
angka= x>='0' and x<='9' #untuk mengetahui apakah string itu angka atau bukan

print('Huruf Kapital?',Kapital)
print('Huruf kecil?',kecil)
print('Angka?',angka)
