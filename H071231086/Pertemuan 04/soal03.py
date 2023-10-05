def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


hasil = highestNumber([9, 1, 93, 430, 23, 212, 34])
print(hasil)