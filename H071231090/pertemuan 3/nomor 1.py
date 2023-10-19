fibonacci = int(input("Masukkan angka: "))

a, b = 0, 1
for i in range(fibonacci):
    print(a, end=' ')
    a, b = b, a+b

print()
