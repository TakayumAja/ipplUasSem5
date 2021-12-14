import json


class Kasir:
    stokBarang = {}

    barangPembeli = {}

    def __init__(self):
        pass

    def simpanBeliJson(self):
        with open("beli.json", "w") as beliFileJson:
            json.dump(Kasir.barangPembeli, beliFileJson)

    def isiStok(self):
        with open("stok.json", "r") as stokReadJson:
            stokDict = json.load(stokReadJson)
            for key, value in stokDict.items():
                print("Barang :", key, "Harga:", value)

    def isiKranjang(self):
        print("Isi Belanjaan Anda: ")
        for key, value in Kasir.barangPembeli.items():
            print("BARANG \t:", key)
            for key2 in value:
                print(key2.upper(), "\t:", value[key2])

    def tambahStok(self):
        stokTrue = input("Apa Anda Belum Punya Database Stock?(y/t) ")
        keyStok = input("Masukkan Barang: ")
        valueStok = int(input("Masukkan Harga: "))
        if stokTrue.lower() == "y":
            Kasir.stokBarang.update({keyStok: valueStok})
            with open("stok.json", "w") as stokFileJson:
                json.dump(Kasir.stokBarang, stokFileJson)
                print("=== Database Stock Sudah diBuat!!!===")
        else:
            with open("stok.json", "r") as stokReadJson:
                stokDict = json.load(stokReadJson)
                if keyStok.lower() in stokDict.keys():
                    print("Barang Sudah Ada!!! \nTambahkan Barang Lain!!!")
                    Kasir.tambahStok(self)
                else:
                    stokDict.update({keyStok: valueStok})
                    with open("stok.json", "w") as stokFileJson:
                        json.dump(stokDict, stokFileJson)
                    print("=== Stock Berhasil Ditambahkan :) ===")

    def editStok(self):
        keyStokEdit = input("Masukkan Barang yang Dirubah: ")
        valueStokEdit = int(input("Masukkan Harga: "))
        with open("stok.json", "r") as stokReadJson:
            stokDict = json.load(stokReadJson)
            if keyStokEdit.lower() in stokDict.keys():
                stokDict.update({keyStokEdit: valueStokEdit})
                with open("stok.json", "w") as stokFileJson:
                    json.dump(stokDict, stokFileJson)
                print("=== Stock Berhasil DiRubah :) ===")
            else:
                print("===Stock Barang Tidak Ditemukan!!!===")
                print("===Edit Barang Yang Ada===!!!")
                Kasir.editStok(self)

    def hapusStok(self):
        keyStockHapus = input("Masukkan Nama Barang yang Dihapus: ")
        with open("stok.json", "r") as stokReadJson:
            stokDict = json.load(stokReadJson)
            if keyStockHapus.lower() in stokDict.keys():
                del stokDict[keyStockHapus]
                with open("stok.json", "w") as stokFileJson:
                    json.dump(stokDict, stokFileJson)
                print("=== Stock Berhasil Dihapus :) ===")
            else:
                print("===Stock Barang Tidak Ditemukan!!!===")
                print("===Hapus Barang Yang Ada===!!!")
                Kasir.hapusStok(self)

    def beliStock(self, keyStokBeli, jmlhStokBeli):
        with open("stok.json", "r") as stokReadJson:
            stokDict = json.load(stokReadJson)
            Kasir.barangPembeli.update(
                {keyStokBeli: {"jumlah": jmlhStokBeli, "harga": stokDict[keyStokBeli]}})
            print("===Belanja Ditambahkan Kekranjang===")
            Kasir.simpanBeliJson(self)

    def totalIsiKranjang(self):
        totalHarga = 0
        hargaKali = 0
        with open("beli.json", "r") as beliJson:
            stokDict = json.load(beliJson)
            for key, value in stokDict.items():
                harga = float(value["harga"])
                jumlah = int(value["jumlah"])
                hargaKali = harga * jumlah
                print(f"{key} \t: {harga} * {jumlah} = {hargaKali}")
                totalHarga += hargaKali
            print("Harga Total Barang: ", totalHarga)

    # testing fungstion

    def testTotalIsiKranjang(self):
        totalHarga = 0
        hargaKali = 0
        with open("beli.json", "r") as beliJson:
            stokDict = json.load(beliJson)
            for key, value in stokDict.items():
                harga = float(value["harga"])
                jumlah = int(value["jumlah"])
                hargaKali = harga * jumlah
                print(f"{key} \t: {harga} * {jumlah} = {hargaKali}")
                totalHarga += hargaKali
            return totalHarga

    def testIsiKranjang(self, cariVaribel):
        with open("beli.json", "r") as beliJson:
            stokDict = json.load(beliJson)
            if cariVaribel.lower() in stokDict.keys():
                return True
            else:
                return False

    def testIsiStok(self, cariVaribel):
        with open("stok.json", "r") as stokReadJson:
            stokDict = json.load(stokReadJson)
            if cariVaribel.lower() in stokDict.keys():
                return True
            else:
                return False
