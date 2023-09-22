#Nomor 2
input_1 = str(input("Masukkan Input 1=")).lower()
input_2 = str(input("Masukkan input 2=")).lower()
input_3 = str(input("Masukkan input 3=")).lower()


match input_1:
    case "invertebrado":
        if input_2=="inseto":
            if input_3=="hematofago":
                print("pulga")
            elif input_3=="herbivoro":
                print("lagarta")
            else:
                print("invalid input!")
        elif input_2=="anelideo":
            if input_3=="hematofago":
                print("sanguessuga")
            elif input_3=="onivoro":
                print("minhoca")
            else:
                print("invalid input!")
        else:
            print("invalid input!")

    case "vertebrado":
        if input_2=="ave":
            if input_3=="cornivoro":
                print("aguia")
            elif input_3=="onivoro":
                print("pomba")
            else:
                print("invalid input!")
        elif input_2=="mamifero":
            if input_3=="onivoro":
                print("homem")
            elif input_3=="horbivoro":
                print("vaca")
            else:
                print("invalid input!")
        else:
            print("invalid input!")
    case _:
        print("invalid input!")
        exit()


print("akhir dari program!")