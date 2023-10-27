def maksimun_angka (*angka):
    
    angka_terbesar = int(angka[0])

    for i in angka:
        if int(i) > angka_terbesar:
            angka_terbesar = int(i)

    return angka_terbesar

inputan =input().split()
print(f">>{maksimun_angka(*inputan)}")