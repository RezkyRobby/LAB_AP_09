a = (input("Masukkan Input Pertama = ")).lower()
b = (input("Masukkan Input Kedua = ")).lower()
c = (input("Masukkan Input Ketiga = ")).lower()

match a,b,c:
    case "vertebrado","ave","carnivoro":
        print("agula")
    case "vertebrado","ave","onivoro":
        print("pomba")
    case "vertebrado","mamifero","onivoro":
        print("homem")
    case "vertebrado","mamifero","herbivoro":
        print("vaca")
    case "invertebrado","inseto","hematofago":
        print("pulga")
    case "invertebrado","inseto","herbivoro":
        print("lagarta")
    case "invertebrado","anelideo","hematofago":
        print("sanguessuga")
    case "invertebrado","anelideo","onivoro":
        print("minhoca")
    case _:
        print("Invalid input")
    