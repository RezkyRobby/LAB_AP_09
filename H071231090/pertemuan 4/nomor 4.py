def catAndMouse(catA, catB, mosC):
    jarak_A_ke_tikus = abs(catA - mosC)
    jarak_B_ke_tikus = abs(catB - mosC)
    
    if jarak_A_ke_tikus < jarak_B_ke_tikus:
        return "Cat A"
    elif jarak_B_ke_tikus < jarak_A_ke_tikus:
        return "Cat B"
    else:
        return "Mouse C"
    
catA = int(input("Posisi Kucing A = "))
catB = int(input("Posisi Kucing B = "))
mosC = int(input("Posisi Tikus = "))
print(catAndMouse(catA, catB, mosC))