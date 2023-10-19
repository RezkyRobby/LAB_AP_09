# while True:
#     try:
#         derajat = float(input(""))
#         total_detik = int((derajat*240)+(6*3600)) 
#         if total_detik >= (24*3600):
#             total_detik = total_detik - (24*3600)
#         jam = total_detik // 3600
#         menit = total_detik % 3600 // 60
#         detik = total_detik % 60

#         if jam >= 24 :
#             jam -= 24

#         if 6 <= jam < 12:
#             print("Selamat pagi")
#         elif 12 <= jam < 15:
#             print("Selamat siang")
#         elif 15 <= jam < 18:
#             print("Selamat sore")
#         else:
#             print("Selamat malam")

#         print(f"{jam:02}:{menit:02}:{detik:02}")

#     except ValueError:
#         print("End of file")
#         break 


while True:
    try:
        derajat = float(input(""))
        total_detik = int(derajat * 240 + 21600) % 86400
        jam = total_detik // 3600
        menit = total_detik % 3600 // 60
        detik = total_detik % 60

        if 3 <= jam < 12:
            print("Selamat pagi")
        elif 12 <= jam < 15:
            print("Selamat siang")
        elif 15 <= jam < 18:
            print("Selamat sore")
        else:
            print("Selamat malam")
        print(f"{jam:02}:{menit:02}:{detik:02}")
        
    except:
        print("End of file")
        break