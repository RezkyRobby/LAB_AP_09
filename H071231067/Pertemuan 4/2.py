def palindrom(kalimat: str) -> bool:
    kalimat_kecil = kalimat.lower()
    kalimat_terbalik = kalimat_kecil[::-1]
    if kalimat_kecil == kalimat_terbalik:
        return 'Palindrom'
    else:
        return 'Bukan Palindrom'


kalimat = input('Masukkan sebuah string= ')
print(f'Palindrom({kalimat})')
print(palindrom(kalimat))
