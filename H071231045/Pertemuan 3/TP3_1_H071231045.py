x = 0
y = 1

n = int(input())
for i in range (n):
    print(x, end ='')
    z = x + y
    x = y
    y = z   