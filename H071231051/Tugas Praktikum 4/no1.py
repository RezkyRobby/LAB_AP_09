try:
    def inputan():
        kata = input()
        return kata

    def permutasi(kata):
        permutasilist = []
        for i in range(len(kata)):
          permutasilist.append(kata)
          kata = kata [1:] + kata [0]
          
        permutasilist.reverse()
        return permutasilist

    hasil_inputan = inputan()
    hasil_permutasi = permutasi(hasil_inputan)

    for hasil in hasil_permutasi:
        print(hasil, end = " | ")

except:
    print("Error, Inputan invalid")
    
    
    
    
    # result1 = permutasi(kata = 'Mobil')
    # for i in result1:
    #     print(i, end = " | ")

    # result2 = permutasi(kata = 'Ayam')
    # for k in result2:
    #     print(k, end = " | ")