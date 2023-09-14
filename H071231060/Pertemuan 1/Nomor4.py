karakter = input("masukkan karakter=")

kapital = karakter >= 'A' and karakter <= 'Z'
huruf_kecil = karakter >= 'a'and karakter <= 'z'
digit = karakter >= '0' and karakter <= '9'
print(f"karakter tersebut adalah huruf besar: {kapital}")
print(f"karakter tersebut adalah huruf kecil: {huruf_kecil}")
print(f"karakter tersebut adalah angka: {digit}")