def permutasi(karakter):
    try:
        permutation_list = []

        for i in range(len(karakter)):
            permutation = karakter [i:] + karakter [:i]
            permutation_list.append(permutation)

        print("|".join(permutation_list[::-1]))

    except:
        print("Error, invalid input")

kata = input("Kata: ")
permutasi(kata)