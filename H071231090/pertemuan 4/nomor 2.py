def palindrom(karakter: str) -> str:

    karakter = karakter.replace(" ", "").lower()

    if karakter == karakter[::-1]:
        return "Polindrom"
    else:
        return "Bukan palindrom"
    
kata = str(input("Masukkan sebuah kata: "))
print(palindrom(kata))