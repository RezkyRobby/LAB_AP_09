print('Konversi detik ke jam')

x=input('Masukkan jumlah detik: ')
x=int(x)

jam=x//3600 # mencari nilai bulat dari pembagian 3600
sisa_detik=x%3600 # mencari nilai sisa dari pembagian 60
menit=sisa_detik//60 #mencari nilai bulat dari pembagian 60
detik=sisa_detik%60 #mencari nilai sisa dari pembagian 60

waktu_format = f"{jam:02d}:{menit:02d}:{detik:02d}" # Mengonversi hasil ke format "00:00:00", 02d dipake agar format 00:00:00 dapat terbentuk

print(waktu_format)