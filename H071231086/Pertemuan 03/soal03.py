# Membaca input dengan looping
while True:
    try:
        derajat = float(input())
        
        # Konversi derajat ke waktu
        total_seconds = (derajat / 360) * 24 * 3600
        total_seconds += 6 * 3600  # Menghitung waktu dari jam 6:00:00
        total_seconds %= 24 * 3600  # Menghindari nilai lebih dari 24 jam
        hours = int(total_seconds // 3600)
        total_seconds %= 3600
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)

        # Menentukan keterangan waktu
        if hours < 6:
            greeting = 'Selamat Malam'
        elif hours < 12:
            greeting = 'Selamat Pagi'
        elif hours < 15:
            greeting = 'Selamat Siang'
        elif hours < 18:
            greeting = 'Selamat Sore'
        else:
            greeting = 'Selamat Malam'

        # Cetak hasil
        print(greeting)
        print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
        exit()
    except EOFError:
        break
