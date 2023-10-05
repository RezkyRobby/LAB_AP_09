def palindrom(karakter: str) -> str:

    karakter = karakter.replace(" ", "").lower()
    
    if karakter == karakter[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

kata = str(input("Masukkan sebuah kata: "))
print(palindrom(kata))