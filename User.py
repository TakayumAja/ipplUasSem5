class User:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan(self):
        print(self.nama)


class Pemilik(User):
    def __init__(self, nama):
        super().__init__(nama)
        self.nama = "asraf"
        self.password = "admin123"


class Pembeli(User):
    def __init__(self, nama):
        super().__init__(nama)
