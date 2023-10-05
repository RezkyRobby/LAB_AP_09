def permutasi(karakter):
    try:
        permutations_list = []

        for i in range(len(karakter)):
            permutation = karakter [i:] + karakter[:i]
            permutations_list.append(permutation)

        print(" | ".join(permutations_list[::-1]))

    except:
        print("Error, invalid input")

kata = input("Kata: ")
permutasi(kata)