while True:
    try:
        derajat = float(input())
    
        total_detik = (derajat / 360) * 24 * 3600
        total_detik += 6 * 3600  
        total_detik %= 24 * 3600 
        jam = int(total_detik // 3600)
        total_detik %= 3600
        menit = int(total_detik // 60)
        detik = int(total_detik % 60)

        if jam < 6:
            ucapan = 'Selamat Malam'
        elif jam < 12:
            ucapan = 'Selamat Pagi'
        elif jam < 15:
            ucapan = 'Selamat Siang'
        elif jam < 18:
            ucapan = 'Selamat Sore'
        else:
            ucapan = 'Selamat Malam'

        print(ucapan)
        print(f'{jam:02d}:{menit:02d}:{detik:02d}')
        exit()
    except EOFError:
        break