a = (input("Golongan = ")).upper()
b = int(input("Daya = "))
c = int(input("Pemakaian = "))

if a == "R1":
    if b == 900:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1352}")
    elif b == 1300:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1444.70}")
    elif b == 2200:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1444.70}")
    else:
        print("data tidak valid")
elif a == "R2":
    if b >= 3500 and b <= 5500:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1699.53}")
    else:
        print("data tidak valid")
elif a == "R3":
    if b >= 6600:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1699.53}")
    else:
        print("data tidak valid")
elif a == "B2":
    if b >= 6600 and b <= 200000:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1444.70}")
    else:
        print("data tidak valid")
elif a == "B3":
    if b > 200000:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1114.74}")
    else:
        print("data tidak valid")
elif a == "I3":
    if b >= 200000:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1314.12}")
    else:
        print("data tidak valid")
elif a == "P1":
    if b >= 6600 and b <= 200000:
        print(f"Jumlah tagihan anda sebesar : Rp.{c*1523.28}")
    else:
        print("data tidak valid")
else:
    print("data tidak valid")

         