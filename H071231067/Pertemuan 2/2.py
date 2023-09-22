x=input('Masukkan Input Pertama : ')
x=x.lower()
y=input('Masukkan Input Kedua : ')
y=y.lower()
z=input('Masukkan Input Ketiga : ')
z=z.lower()

match x:
    case 'vertebrado':
        if y=='ave':
         if z=='carnivoro':
          print('aguia')
         elif z=='onivoro':
          print('pomba')
          
        elif y=='mamifero':
         if z=='onivoro':
          print('homem')
         elif z=='herbivoro':
          print('vaca')
        else:print('Invalid input')
    
    case 'invertebrado':
        if y=='inseto':
         if z=='hematofago':
          print('pulga')
         elif z=='herbivoro':
          print('lagarta')
          
        elif y=='anelideo':
         if z=='hematofago':
          print('sanguessuga')
         elif z=='onivoro':
          print('minhoca')
        else:print('Invalid Input')
    case _:
          print('Invalid input')