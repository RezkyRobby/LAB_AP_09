import re

username = input("Masukkan username: ")

# Validasi username
def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.match(pattern, username)

# Validasi email
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9]{5,}@[A-Za-z0-9]+\.(com|co\.id)$"
    return re.match(pattern, email)

# Validasi password
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.match(pattern, password)

# Input email
email = input("Masukkan email: ")

# Validasi email
if is_valid_username(username) and is_valid_email(email):
    # Input password
    password = input("Masukkan password: ")

    # Validasi password
    if is_valid_password(password):
        # Registrasi berhasil
        print("\nRegistrasi berhasil! Halo", username)
    else:
        # Password tidak memenuhi syarat
        print("\nPassword yang Anda masukkan berisiko dihack. Registrasi gagal.")
else:
    # Username atau email tidak valid
    print("\nUsername atau email yang Anda masukkan tidak valid dalam sistem. Registrasi gagal!")