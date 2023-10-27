# Persamaan kuadrat
a = float (input('input nilai a : '))
if a==0:
    print ('inputan tidak valid')
    exit()
b = float(input('input nilai b : '))
c = float(input('input nilai c : '))

#masukkan rumus persamaan
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a) 
print(f'x1 = {x1: .2f}')
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a) 
print(f'x2 = {x2: .2f}')

