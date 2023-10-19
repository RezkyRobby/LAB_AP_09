golongan = (input("Golongan = "))
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

if golongan == "R1" and daya == 1352:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1352:,.2f}")
elif golongan == "R1" and daya >= 1300 and daya <= 2200:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1444.70:,.2f}")
elif golongan == "R2" and daya >= 3500 and daya <= 5500:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1699.53:,.2f}")
elif golongan == "R3" and daya >= 6600:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1699.53:,.2f}")
elif golongan == "B2" and daya >= 6600 and daya <= 200000:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1444.70:,.2f}")
elif golongan == "B3" and daya >= 200000:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1114.74:,.2f}")
elif golongan == "I3" and daya >= 200000:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1314.12:,.2f}")
elif golongan == "P1" and daya >= 6600 and daya <= 200000:
    print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {pemakaian*1523.28:,.2f}")
else:
    print("data tidak valid")
