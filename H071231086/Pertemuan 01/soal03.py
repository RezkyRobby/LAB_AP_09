while True:
    a = int(input("input a = "))
    if a ==0:
        print("input a tidak boleh 0 !")
    else:
        break

b = int(input("input b = "))
c = int(input("input c = "))

x1 = (-b + ((b*b)-(4*a*c)))/2*a
x2 = (-b - ((b*b)-(4*a*c)))/2*a

print (f'x1 = {x1:.2f}')
print (f'x1 = {x2:.2f}')