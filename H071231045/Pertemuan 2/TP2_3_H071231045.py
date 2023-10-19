golongan =(input('Golongan : '))
daya =int(input('Daya : '))
pemakaian =int(input('Pemakaian : '))

match golongan:
    case 'R1':
        if daya == 900:
            tagihan = 1352*pemakaian
        elif daya == 1300:
            tagihan = 1444.70*pemakaian
        elif daya == 2200:
            tagihan = 1444.70*pemakaian
    case 'R2':
        if 3500 <= daya <= 5500:
            tagihan = 1699.53*pemakaian 
    case 'R3':
        if daya >= 6600:
            tagihan = 1699.53*pemakaian
    case 'B2':
        if 6600 <= daya <= 200000:
            tagihan = 1444.70*pemakaian
    case 'B3':
        if daya >= 200000:
            tagihan = 1114.74*pemakaian
    case 'I3':
        if daya >= 200000:
            tagihan = 1314.12*pemakaian
    case 'P1':
        if 66000 <= daya <= 2000000:
            tagihan = 1114.74*pemakaian
    case _:
        print('input tidak valid') 

print(f'Rp, {tagihan:,.2f}'.replace(',','x').replace('.',',').replace('x','.'))