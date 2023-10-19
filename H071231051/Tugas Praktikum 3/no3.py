while True:
    M = float(input())
    if 0 <= M < 360:
        break
    else:
        print("End Of File")
    
detik = int(M * 240)
jam = detik // 3600 + 6

if jam >= 24:
    jam = jam % 24
        
menit = detik % 3600//60
detik = detik % 60

if jam >= 6 and jam < 12:
    waktu_selamat = "Selamat Pagi"
elif jam >= 12 and jam < 15:
    waktu_selamat = "Selamat Siang"
elif jam >= 15 and jam < 18:
    waktu_selamat = "Selamat Sore"
else:
    waktu_selamat = "Selamat Malam"

print(waktu_selamat)
print(f"{jam:02}:{menit:02}:{detik:02}")