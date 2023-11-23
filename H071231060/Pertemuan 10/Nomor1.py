import re

class DataPengguna:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}

    def tampilkan_detail(self):
        if not self.data['Nama']:
            print("Data saat ini kosong")
        else:
            print("Detail Data:")
            [print(f"{key}: {value}") for key, value in self.data.items()]

    def ubah_nama(self):
        if not self.data['Nama']:
            print("Data saat ini kosong")
        else:
            self.data['Nama'] = input("Masukkan nama baru: ")
            print("Nama berhasil diubah")

    def validasi_email(self, email):
        return re.match(r"[a-z0-9._%+-]+@student.unhas.ac.id$", email)

    def validasi_password(self, password):
        return 8 <= len(password) <= 20 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

    def buat_data_baru(self):
        self.data['Nama'] = input("Masukkan Nama: ")

        while True:
            email = input("Masukkan Email: ")
            if self.validasi_email(email):
                break
            else:
                print("Email yang Anda Masukkan Salah")

        while True:
            password = input("Masukkan Password: ")
            if self.validasi_password(password):
                break
            else:
                print("Password yang Anda masukkan terlalu lemah. Gunakan minimal 1 huruf kapital, huruf kecil, dan angka.")

        self.data['Email'], self.data['Password'] = email, password
        print("Data berhasil dibuat")

    def simpan_data_ke_file(self):
        nama_file = input("Masukkan nama file tanpa format '.txt': ") + '.txt'

        with open(nama_file, 'a') as file:
            if not self.data['Nama']:
                print("Data saat ini kosong")
                return

            if not file.tell():
                file.write("+" + "=" * 55 + f"\n| Data yang Tersimpan\n+{'=' * 55}")

            [file.write(f"\n| {key.ljust(10)}: {value}") for key, value in self.data.items()]
            file.write("\n+" + "=" * 55)
            self.data = {'Nama': '', 'Email': '', 'Password': ''}

        print("Berhasil menyimpan data pada file")

def Jumlah_data(nama_file):
    try:
        with open(nama_file, 'r') as file:
            jumlah_data = sum(1 for line in file if re.match(r"[| Nama]+[ ]+:+", line))
        print(f"Jumlah data pada file {nama_file}: {jumlah_data}")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {nama_file}")

def main():
    data_pengguna = DataPengguna()

    while True:
        print("\nMenu:\n" + '\n'.join([f"{i + 1}. {menu}" for i, menu in enumerate(['Tampilkan Detail Anda', 'Ubah Nama', 'Jumlah Data pada File', 'Simpan Data pada File', 'Buat Data Baru', 'Keluar'])]))
        pilihan = input("Pilih menu (1-6): ")

        match pilihan:
            case '1':
                data_pengguna.tampilkan_detail()
            case '2':
                data_pengguna.ubah_nama()
            case '3':
                Jumlah_data(input("Masukkan nama file tanpa format '.txt': ") + '.txt')
            case '4':
                data_pengguna.simpan_data_ke_file()
            case '5':
                data_pengguna.buat_data_baru()
            case '6':
                print("Sampai Jumpa Lagi")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu (1-6)")

if __name__ == "__main__":
    main()