def maksimum(list_angka):
    nilai_maksimum = list_angka[0]
    for x in list_angka:
        if x > nilai_maksimum:
            nilai_maksimum = x
    return nilai_maksimum


try:
    angka = (input('Masukkan angka = '))
    list_angka = [int(angka) for angka in angka.split(',')]
    list_tanpa_kurung_siku = str(list_angka).replace(
        '[', '(').replace(']', ')')
    print(f'Maksimum{list_tanpa_kurung_siku}')
    print(f'>> {maksimum(list_angka)}')
except ValueError as pesan:
    print('Terjadi Kesalahan =', pesan)
