x=input('Masukkan Input Pertama : ').lower()
y=input('Masukkan Input Kedua   : ').lower()
z=input('Masukkan Input ketiga  : ').lower()

match (x, y, z) :
    case('vertebrado', 'ave', 'carnivoro'):
        print('aguia')
    case('vertebrado', 'ave', 'onivoro'):
        print('pomba')
    case('vertebrado', 'mamifero', 'onivoro'):
        print('homem')
    case('vertebrado', 'mamifero', 'herbivoro'):
        print('vaca')
    case('invertebrado', 'inseto', 'hematofago'):
         print('pulga')
    case('invertebrado', 'inseto', 'herbivoro'):
        print('lagarta')
    case('invertebrado', 'anelideo', 'hematofago'):
        print('sanguessuga')
    case('invertebrado', 'anelideo', 'onivoro'):
        print('minhoca')
    case _:
        print('input tidak valid')
    