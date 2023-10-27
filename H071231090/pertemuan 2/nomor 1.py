print("Pilih Gender Anda")
print("1. pria")
print("2. Wanita")
gender = int(input("= "))

tinggi_badan = float(input("Masukkan tinggi badan (cm) : "))
berat_badan = float(input("Masukkan berat badan (kg) : "))

tinggi_m = tinggi_badan / 100

BMI = berat_badan / (tinggi_m) ** 2

if gender == 1:
    if BMI <18:
        tergolong = "Underweight"
    elif 18 <= BMI < 24:
        tergolong = "Normal"
    elif 24 <= BMI < 27:
        tergolong = "Overweight"
    else:
        tergolong = "obese"

if gender == 2:
    if BMI <17:
        tergolong = "Underweight"
    elif 17 <= BMI < 24:
        tergolong = "Normal"
    elif 24 <= BMI < 28:
        tergolong = "Overweight"
    else:
        tergolong = "obese"

if tergolong:
    print(F"Anda tergolong {tergolong} dengan BMI {BMI:.2f}")
else:
    print("Jenis Kelamin tidak valid")