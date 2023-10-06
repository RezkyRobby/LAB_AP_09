def maksimun_angka (*angka):
    if not angka:
        return None
    
    angka_terbesar = angka[0]

    for i in angka:
        if i > angka_terbesar:
            angka_terbesar = i

    return angka_terbesar

inputan =input()
angka = [int(a) for a in inputan.split()]
print(f">>{maksimun_angka(*angka)}")