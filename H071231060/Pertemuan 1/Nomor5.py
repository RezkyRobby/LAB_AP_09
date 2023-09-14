Detik = int(input("masukkan detik="))
jam = Detik // 3600
Detik %= 3600
menit = Detik // 60
Detik %= 60
print(f"Jadi setelah di konversi akan menjadi {jam:02}:{menit:02}:{Detik:02}")
