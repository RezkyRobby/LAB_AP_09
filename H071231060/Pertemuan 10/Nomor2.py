class Motor:
    def __init__(self, merk, jenis, harga):
        self.merk = merk
        self.jenis = jenis
        self.harga = harga

    def deskripsi(self):
        return f"{self.merk} {self.jenis} dengan harga {self.harga}."

class Yamaha(Motor):
    def __init__(self, jenis, harga):
        super().__init__('Yamaha', jenis, harga)

class Honda(Motor):
    def __init__(self, jenis, harga):
        super().__init__('Honda', jenis, harga)

class Suzuki(Motor):
    def __init__(self, jenis, harga):
        super().__init__('Suzuki', jenis, harga)

motor_yamaha = Yamaha('Mio', 15000000)
motor_honda = Honda('Beat', 14000000)
motor_suzuki = Suzuki('Nex', 16000000)

motors = [motor_yamaha, motor_honda, motor_suzuki]

for motor in motors:
    print(motor.deskripsi())