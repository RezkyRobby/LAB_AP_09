while True:
    a=input('Input a = ')
    a=float(a)
    if a!=0:break  #agar angka yang dimasukkan tidak 0                 
    else:print('angka tidak boleh 0')

b=input('Input b = ')
b=float(b)

c=input('Input c = ')
c=float(c)

x1=(-b+((b**2-4*a*c)**0.5))/(2*a)#rumus untuk x1
if isinstance(x1,complex):
    print('x1 bukan bilangan real')
else:
    print('x1 =',format(x1,'.2f'))

x2=(-b-((b**2-4*a*c)**0.5))/(2*a) #rumus untuk x2
if isinstance(x2,complex):
    print('x2 bukan bilangan real')
else:
    print('x2 =',format(x2,'.2f'))