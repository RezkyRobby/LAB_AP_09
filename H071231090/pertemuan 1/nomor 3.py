a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

if a==0:
    print("Masukkan Selain 0")
else:
    X1 = (-b+((b**2)-(4*a*c)))/(2*a)
    X2 = (-b-((b**2)-(4*a*c)))/(2*a)
    print(f"X1 : {X1:.2f}")
    print(f"X2 : {X2:.2f}")

# d = (b**2)-(4*a*c)