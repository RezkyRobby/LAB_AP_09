print("Konversi detik ke jam")
detik_awal = int(input("Masukkan jumlah detik: "))

jam = detik_awal//3600
menit = (detik_awal-(jam*3600))//60
detik = (detik_awal-(jam*3600)-(menit*60))

print(f"{jam:02}:{menit:02}:{detik:02}")