g = int(input("Pilih Gender Anda\n 1. Pria\n 2. Wanita\n = "))
tb = float(input("Masukkan tinggi badan (cm)= "))
bb = float(input("Masukkan berat badan (kg) = "))

bmi = bb / (tb/100)**2

if g == 1 :
    if bmi <18 :
        print(f"Anda tergolong Underweight dengam BMI {bmi:.2f}")
    elif bmi >=18 and bmi <=23.9 :
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >=24 and bmi <=26.9 :
        print(f"Anda tergolong Overweight dengan BMi {bmi:.2f}")
    elif bmi >=27 :
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
  
elif g == 2 :
    if bmi <17 :
        print(f"Anda tergolong Underweight dengam BMI {bmi:.2f}")
    elif bmi >=17 and bmi <=23.9 :
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >=24 and bmi <=27.9 :
        print(f"Anda tergolong Overweight dengan BMi {bmi:.2f}")
    elif bmi >=28 :
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
else:
    print("Gender tidak valid")
        


