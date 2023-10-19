print('Pilih Gender Anda')
print('1. Pria')
print('2. Wanita')
while True:
   golongan=input('= ')
   golongan=int(golongan)
   golongan1=[1,2]
   if golongan in golongan1 :break                
   else:print('hanya boleh antara 1 atau 2')


tinggi=input('Masukkan tinggi badan (cm) : ')
tinggi=float(tinggi)

berat=input('Masukkan berat badan (kg) : ')
berat=float(berat)

BMI=(berat/(tinggi/100)**2)

match golongan:
    case 1:
        if BMI<18:
         print('Anda tergolong Underweight dengan BMI',format(BMI,'.2f'))
        elif BMI>=18 and BMI<=23.9:
         print('Anda tergolong Normal dengan BMI',format(BMI,'.2f'))
        elif BMI>=24 and BMI<=26.9:
         print('Anda tergolong Overweight dengan BMI',format(BMI,'.2f'))
        elif BMI>=27:
         print('Anda tergolong Obese dengan BMI',format(BMI,'.2f'))
    
    case 2:
        if BMI<17:
         print('Anda tergolong Underweight dengan BMI',format(BMI,'.2f'))
        elif BMI>=17 and BMI<=23.9:
         print('Anda tergolong Normal dengan BMI',format(BMI,'.2f'))
        elif BMI>=24 and BMI<=27.9:
         print('Anda tergolong Overweight dengan BMI',format(BMI,'.2f'))
        elif BMI>=28:
         print('Anda tergolong Obese dengan BMI',format(BMI,'.2f'))