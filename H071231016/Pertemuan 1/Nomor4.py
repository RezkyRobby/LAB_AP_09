#Penentuan karakter huruf
karakter = input('Input karakter:')

Kapital = karakter >= 'A' and karakter <= 'Z'
huruf_kecil = karakter >= 'a' and karakter <= 'z'
digit = karakter >= '0' and karakter <= '9'

print("Huruf Kapital?", Kapital)
print("Huruf Kecil?", huruf_kecil)
print("Angka?",digit)
