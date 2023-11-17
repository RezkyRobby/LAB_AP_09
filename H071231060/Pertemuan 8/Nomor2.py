import re

def tentukan_ip(n, hasil):
    if n == 0:
        False
    else:
        inputan = input().strip()
        pattern_1 = r'^(\d{1,3}\.){3}\d{1,3}$'
        pattern_2 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        ipv4 = re.match(pattern_1, inputan)
        ipv6 = re.match(pattern_2, inputan)
        if ipv4 and all(0 <= int(bagian) <= 255 for bagian in ipv4.group().split('.')):
            hasil.append("IPv4")
        elif ipv6:
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")
        tentukan_ip(n - 1, hasil)

n = int(input("N: "))
hasil = []
tentukan_ip(n, hasil)
for i in hasil:
    print(i)