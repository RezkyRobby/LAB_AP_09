print("Pengujian jenis karakter")
print("------------------------")
x = input("Karakter: ")

# h_kapital = "Huruf kapital? True\nHuruf kecil? False\nAngka? False"
# h_kecil = "Huruf kapital? False\nHuruf kecil? True\nAngka? False"
# angka = "Huruf kapital? False\nHuruf kecil? False\nAngka? True"

# if x.isupper():
#     print(h_kapital)
# elif x.islower():
#     print(h_kecil)
# elif x.isdigit():
#     print(angka)


kapital = x>="A" and x<="Z"
kecil = x>="a" and x<="z"
angka = x>="0" and x<="9"

print("Huruf Kapital?", kapital)
print("Huruf kecil?", kecil)
print("Angka?", angka)