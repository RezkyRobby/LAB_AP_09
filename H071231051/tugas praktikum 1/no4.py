print("Pengujian jenis karakter\n-----------------------")
x = (input("Masukkan sebuah karakter: "))

Hurufkapital = x >= 'A' and x <= 'Z'
Hurufkecil = x >= 'a' and x <= 'z'
Angka = x >= '0' and x <= '9'

print(f"Huruf kapital? {Hurufkapital}")
print(f"Huruf keci? {Hurufkecil}")
print(f"Angka? {Angka}")