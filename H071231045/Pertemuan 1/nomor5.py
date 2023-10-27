print('Konversi Detik ke Jam')
 
d = int(input('Masukkan jumlah detik : '))

jam =(d//3600)
menit =(d-(jam*3600))//60
detik =(d-(jam*3600)-(menit*60))

print(f'{jam:02}:{menit:02}:{detik:02}')