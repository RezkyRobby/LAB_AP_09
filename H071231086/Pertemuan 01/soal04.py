print('Pengujian jenis karakter')
x = input('Karakter = ')

# angka = "Huruf kapital? False\nHuruf kecil? False\nAngka? True"
# h_besar = "Huruf kapital? True\nHuruf kecil? False\nAngka? False"
# h_kecil = "Huruf kapital? False\nHuruf kecil? True\nAngka? False"

# if x.isupper():
#     print(h_besar)
# elif x.islower():
#     print(h_kecil)
# elif x.isdigit():
#     print(angka)
kapital = x>="A"and x<="Z"
kecil = x>="a"and x<="z" 
angka = x>="0"and x<="9"

print("huruf kapital?", kapital)
print("huruf kecil?", kecil)
print("angka?", angka)
