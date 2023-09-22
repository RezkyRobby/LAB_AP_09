input1 = input("Masukkan Inputan Pertama : ").replace(" ","").lower()
input2 = input("Masukkan Inputan Kedua : ").replace(" ","").lower()
input3 = input("Masukkan Inputan Ketiga : ").replace(" ","").lower()

if input1 == 'vertebrado':
    if input2 == 'ave':
        if input3 =='carnivoro':
            print("agula")
        elif input3 == 'onivoro':
            print("pomba")
        else:
            print("Invalid Input")
    elif input2 == 'mamifero':
        if input3 =='hematofogo':
            print("homem")
        elif input3 == 'herbivoro':
            print("vaca")
        else:
          print("Invalid Input")
    else:
        print("Invalid Input")

elif input1 == 'invertebrado':
    if input2 == 'inseto':
        if input3 =='hematofogo':
            print("pulga")
        elif input3 == 'herbivoro':
            print("isgarta")
        else:
            print("Invalid Input")

    elif input2 == 'aniledeo':
        if input3 =='hematofogo':
            print("sanguessuga")
        elif input3 == 'onivoro':
            print("minhoca")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")
