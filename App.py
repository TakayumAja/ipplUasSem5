from User import Pemilik, Pembeli
from Kasir import Kasir


def login():
    print("""
    === Login Sebagai Siapa ===
            1. Pemilik
            2. Pembeli
    """)
    user = int(input("Masuk Sebagai Siapa, Masukkan Angka 1/2: "))
    if user == 1:
        nama = input("Masukkan Nama: ")
        password = input("Masukkan Password: ")
        Pemilik1 = Pemilik(nama)
        if Pemilik1.password == password and Pemilik1.nama == nama:
            print("Anda Admin :)")
            menuPemilik()

        else:
            print("Anda Bukan Admin, Login Lagi!!!")
            login()
    else:
        nama = input("Masukkan Nama: ")
        Pembeli1 = Pembeli(nama)
        menuPembeli()


def menuPemilik():
    print("""
    ==== Menu Pemilik ===
    1. Tambahkan Stok
    2. Edit Stok
    3. Hapus Stok
    4. Tampilkan Stok
    5. Keluar
        """)
    menu = int(input("Masukkan Angka Menu: "))
    Kasir1 = Kasir()
    if menu == 1:
        print("=+= Tambah Stok =+=")
        Kasir1.tambahStok()
        menuPemilik()
    elif menu == 2:
        print("=+= Edit Stok =+=")
        Kasir1.editStok()
        menuPemilik()
    elif menu == 3:
        print("=+= Hapus Stok =+=")
        Kasir1.hapusStok()
        menuPemilik()
    elif menu == 4:
        Kasir1.isiStok()
        menuPemilik()
    elif menu == 5:
        print("Trimakasih :) ")
        exit
    else:
        print("Daftar Menu Tidak Ditemukan!!!")
        print("=*= Pilih Menu Lagi!!! =*= \n")
        menuPemilik()


def menuPembeli():
    print("""
    === Menu Pembeli ===
    1. Tambahkan Belanjaan
    2. Bayar Belanjaan
    3. Keluar
    """)
    menu = int(input("Masukkan Angka Menu: "))
    Kasir2 = Kasir()
    if menu == 1:
        Kasir2.isiStok()
        keyStokBeli = input("Masukkan Nama Barang: ")
        jmlhStokBeli = int(input("Masukkan Jumlah Barang: "))
        Kasir2.beliStock(keyStokBeli.lower(), jmlhStokBeli)
        menuPembeli()
    elif menu == 2:
        Kasir2.isiKranjang()
        Kasir2.totalIsiKranjang()
        exit
    elif menu == 3:
        exit
    else:
        print("Menu Tidak Ditemukan!!!")
        menuPembeli()
        print("=*= Pilih Menu Lagi!!! =*= \n")


login()
