golongan = input("Golongan = ").upper()
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

if golongan == 'R1' :
    if daya == 900 :
        tarif = 1352
    elif daya == 1300 or daya == 2200:
        tarif = 1444.70
elif golongan == 'R2' and daya >= 3500 and daya <= 5500:
    tarif = 1699.53
elif golongan == 'R3' and daya >= 6600:
    tarif = 1699.53
elif golongan == 'B2' and daya >= 6600 and daya <= 200000:
    tarif = 1444.70
elif golongan == 'B3' and daya >= 200000:
    tarif = 1114.74
elif golongan == 'I3' and daya >= 200000:
    tarif = 1314.12
elif golongan == 'P1' and daya >= 6600 and daya <= 200000:
    tarif = 1523.28
else:
    print("Invalid Input")
    exit()

tagihan = tarif * pemakaian
tagihan_rupiah = f"{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x",".") 
print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {tagihan_rupiah}")