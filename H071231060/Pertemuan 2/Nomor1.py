#Nomor 1
gender = int(input("Pilih gender anda:\n1. Laki-Laki \n2. Perempuan \n="))
tinggi_badan = float(input("Masukkan tinggi badan anda (cm) ="))
TB_fix = tinggi_badan/100
berat_badan = float(input("Masukkan berat badan anda (kg) ="))
Bmi = berat_badan/TB_fix**2

match gender:
    case 1 :
        if Bmi<=18:
            print(f"Anda tergolong Under weight Dengan BMI =", format (Bmi, ".2f"))
        elif Bmi>18 and Bmi<=23.9 :
            print(f"anda tergolong normal dengen BMI =", format (Bmi, ".2f"))
        elif Bmi>24 and Bmi<=26.9 :
            print(f"Anda tergolong over weight dengan BMI =", format (Bmi, ".2f"))
        else:
            print(f"anda tergolong obesitas dengan BMI =", format(Bmi, ".2f" ))
    case 2:
        if Bmi<=17:
            print(f"Anda tergolong Under weight Dengan BMI =", format (Bmi, ".2f"))
        elif Bmi>17 and Bmi<=23.9 :
            print(f"anda tergolong normal dengen BMI =", format (Bmi, ".2f"))
        elif Bmi>24 and Bmi<=27.9 :
            print(f"Anda tergolong over weight dengan BMI =", format (Bmi, ".2f"))
        else:
            print(f"anda tergolong obesitas dengan BMI =", format(Bmi, ".2f" ))
