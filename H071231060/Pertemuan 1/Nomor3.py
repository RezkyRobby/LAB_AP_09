#angka yang dimasukkan tidak boleh 0
a = float(input("masukkan nilai a="))
b = float(input("masukkan nilai b="))
c = float(input("masukkan nilai c="))

x1 = -b + ((b*b-4*a*c)**0.5)/2*a
print("nilai dari x1 adalah", format (x1, ".2f"))
x2 = -b - ((b*b-4*a*c)**0.5)/2*a
print("nilai dari x2 adalah", format (x2, ".2f"))