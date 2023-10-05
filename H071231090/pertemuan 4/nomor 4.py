def catAndMouse(catA,catB,mosC):
    jarak_catA = abs(catA - mosC)
    jarak_catB = abs(catB - mosC)
    
    if jarak_catA < jarak_catB:
        return "Cat A"
    elif jarak_catB < jarak_catA:
        return "Cat B"
    else:
        return "Mouse C" 
    
catA = int(input("catA: ")) 
catB = int(input("catB: ")) 
mosC = int(input("mosC: "))

print(catAndMouse(catA, catB, mosC))