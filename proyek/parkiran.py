import os
import time

lahan = []
lahan_tersedia = 0
lahan_total = 0
baris = 0

hitung_lahan = 0
tepi = ''
linux = 0

class Kendaraan:
    def __init__(self, tipe, pelat):
        self.tipe = tipe
        self.pelat = pelat
        self.waktu_masuk = time.time()

    def idn_tipe(self):
        return self.tipe

    def idn_tipe_str(self):
        if self.tipe == 1:
            return "Mobil"
        elif self.tipe == 2:
            return "Truk"
        elif self.tipe == 3:
            return "Motor"

    def idn_pelat(self):
        return self.pelat

    def idn_waktu_masuk(self):
        return self.waktu_masuk

    def set_waktu_masuk_baru(self, waktu_baru):
        self.waktu_masuk = waktu_baru

    def idn_kendaraan(self):
        return self.tipe, self.pelat, self.waktu_masuk

class Lahan:
    def __init__(self):
        self.kendaraan = None
        self.occupied = False

    def tambah_kendaraan(self, kendaraan):
        self.kendaraan = kendaraan
        self.occupied = True

    def hapus_kendaraan(self):
        k_keluar = self.kendaraan
        self.kendaraan = None
        self.occupied = False
        return k_keluar

    def info_kendaraan(self):
        return self.kendaraan

    def tersedia(self):
        return self.occupied

def print_baris(row):
    global lahan, hitung_lahan

    output = "|"
    for s in range(hitung_lahan * row, hitung_lahan * (row + 1)):
        if not lahan[s].tersedia():
            output += "[ ]"
        else:
            output += "["
            output += "c" if lahan[s].info_kendaraan().idn_tipe() == 1 \
                else "t" if lahan[s].info_kendaraan().idn_tipe() == 2 \
                else "m"
            output += "]"
        if s < hitung_lahan * (row + 1) - 1:
            output += " "
    output += "|"

    return output

def tampilkan_lahan():
    global lahan, lahan_tersedia, lahan_total, baris

    output = "Area Tersedia: " + str(lahan_tersedia) + "\n"

    output += tepi

    for row in range(baris):
        output += print_baris(row) + "\n"

    output += tepi

    if linux == 1:
        os.system("clear")
    print(output)

def tampilkan_baris_pilihan():
    global lahan, lahan_tersedia, lahan_total, baris

    output = "Area Tersedia: " + str(lahan_tersedia) + "\n"

    output += tepi
    for row in range(baris):
        output += print_baris(row)
        output += " <" + str(row) + ">\n"
    output += tepi

    if linux == 1:
        os.system("clear")
    print(output)

def tampilkan_baris_pilihan():
    global lahan, lahan_tersedia, lahan_total, baris

    output = "Area Tersedia: " + str(lahan_tersedia) + "\n"

    output += tepi
    for row in range(baris):
        output += print_baris(row)
        output += " <" + str(row) + ">\n"
    output += tepi

    if linux == 1:
        os.system("clear")
    print(output)

def tampilkan_lahan_pilihan(row):
    global lahan, lahan_tersedia, lahan_total, baris

    output = "Lihat Baris: " + row + "\n"

    output += tepi
    output += print_baris(int(row)) + "\n"

    output += " "
    for count in range(hitung_lahan):
        if count < 10:
            output += "<" + str(count) + "> "
        else:
            output += "<" + str(count) + ">"

    output += "\n"
    output += tepi

    if linux == 1:
        os.system("clear")
    print(output)

    return hitung_lahan

def kendaraan_masuk(tipe, pelat, row, space):
    global lahan, lahan_tersedia, lahan_total, baris

    if lahan_tersedia == 0:
        tampilkan_lahan()
        print("Error: Tidak ada lahan parkir kosong")
        time.sleep(2)
        return

    if Lahan[(int(row) * hitung_lahan) + int(space)].tersedia():
        tampilkan_lahan_pilihan(row)
        print("Error: Kendaraan sudah terparkir")
        time.sleep(2)
        return -1

    for uniq in Lahan:
        if uniq.tersedia():
            if uniq.info_kendaraan().pelat() == pelat:
                tampilkan_lahan()
                print("Error: Kendaraan sudah terparkir")
                time.sleep(2)
                return
    kendaraan_baru = Kendaraan(tipe, pelat)
    lahan[(int(row) * hitung_lahan) + int(space)].tambah_kendaraan(kendaraan_baru)
    lahan_tersedia -= 1
    tampilkan_lahan()
    print("Kendaraan Ditambahkan ke parkiran\n"
          "Waktu masuk: " + str(time.strftime('%I:%M %p',
                                               time.localtime(kendaraan_baru.set_waktu_masuk()))))
    time.sleep(2)

    return kendaraan_baru

def jumlah_bayar(kendaraan):
    total_time = time.time() - kendaraan.set_waktu_masuk()
    if total_time < 3600:
        hours = 1
    else:
        hours = int(total_time / 3600)+1

    if kendaraan.idn_tipe() == 1:
        rate = hours * 3000
    elif kendaraan.idn_tipe() == 2:
        rate = hours * 5000
    else:
        rate = hours * 2000

    ret = "Kendaraan dikeluarkan\n" \
          "Total untuk " + "{:.2f}".format(hours) + " jam adalah Rp" + "{:.2f}".format(rate)

    return ret

def keluar_lahan(row, space):
    global lahan_tersedia

    if not lahan[(int(row) * hitung_lahan) + int(space)].tersedia():
        tampilkan_lahan_pilihan(row)
        print("Error: Tidak ada kendaraan di lahan")
        time.sleep(2)
        return

    removed = lahan[(int(row) * hitung_lahan) + int(space)].hapus_kendaraan()
    lahan_tersedia += 1

    tampilkan_lahan()
    print(jumlah_bayar(removed))
    time.sleep(2)

def tampilkan_kendaraan(row, space):

    if not lahan[(int(row) * hitung_lahan) + int(space)].tersedia():
        tampilkan_lahan_pilihan(row)
        print("Error: Tidak ada kendaraan dalam lahan")
        time.sleep(2)

    else:
        vehicle = lahan[(int(row) * hitung_lahan) + int(space)].info_kendaraan()
        tampilkan_lahan_pilihan(row)
        input("Tipe kendaraan: " + vehicle.idn_tipe_str() + "\n"
                                                             "Plat Nomor: " + vehicle.idn_pelat() + "\n"
                                                                                                      "Waktu masuk: " + str(
            time.strftime('%m-%d-%Y %I:%M %p',
                          time.localtime(vehicle.set_waktu_masuk()))) + "\n"
                                                                       "\nTekan enter untuk kembali ke menu")

def command_handler(command):
    if command == "P":
        while True:
            tampilkan_lahan()
            new_type = input("Enter Vehicle Type:\n"
                             "1. Mobil\n"
                             "2. Truk\n"
                             "3. Motor\n"
                             ">")
            if new_type == "1" or new_type == "2" or new_type == "3":
                break
        tampilkan_lahan()
        new_plate = input("Masukan pelat nomor kendaraan:\n"
                          ">")

        ret_val = -1
        while ret_val == -1:
            while True:
                tampilkan_baris_pilihan()
                row = input("Pilih baris yang diinginkan:\n"
                            ">")
                if row.isnumeric():
                    if int(row) < baris:
                        break
            while True:
                tampilkan_lahan_pilihan(row)
                space = input("Pilih lahan untuk parkir:\n"
                              ">")
                if space.isnumeric():
                    if int(space) < hitung_lahan:
                        break
            ret_val = kendaraan_masuk(int(new_type), new_plate, row, space)

    elif command == "E":

        while True:
            tampilkan_baris_pilihan()
            row = input("Pilih baris dari kendaraan:\n"
                        ">")
            if row.isnumeric():
                if int(row) < baris:
                    break

        while True:
            tampilkan_lahan_pilihan(row)
            space = input("Tampilkan lahan kendaraan:\n"
                          ">")
            if space.isnumeric():
                if int(space) < hitung_lahan:
                    break

        keluar_lahan(row, space)

    elif command == "V":

        while True:
            tampilkan_baris_pilihan()
            row = input("Pilih baris yang ingin dilihat:\n"
                        ">")
            if row.isnumeric():
                if int(row) < baris:
                    break

        while True:
            tampilkan_baris_pilihan(row)
            space = input("Pilih lahan yang ingin dilihat:\n"
                          ">")
            if space.isnumeric():
                if int(space) < hitung_lahan:
                    break
        tampilkan_kendaraan(row, space)

    elif command == "R":
        tampilkan_lahan()
        input("Harga Parkir:\n"
              "Mobil - Rp3000/jam\n"
              "Truk  - Rp5000/jam\n"
              "Motor - Rp2000/jam\n"
              "\nTekan Enter untuk kembali ke menu")

    elif command == "Q":
        return

    else:
        tampilkan_lahan()
        print(": Invalid Command")
        time.sleep(1)

def read_config():
    global lahan, lahan_total, lahan_tersedia, baris, linux, hitung_lahan, tepi
    lahan=[]
    lahan_total = 20
    lahan_tersedia = lahan_total
    baris = 10
    linux = 0
    demo_mode = 1
    while True:
        if demo_mode != 1:
            demo_mode()
            break
        else:
            for i in range(lahan_total):
                lahan.append(Lahan())

            hitung_lahan = int(lahan_total / baris)

            tepi = "|"
            for i in range(hitung_lahan - 1):
                for j in range(4):
                    tepi += "-"
            tepi += "---|\n"
            tepi

def demo_mode():
    global lahan, lahan_total, lahan_tersedia, baris, hitung_lahan, tepi

    for i in range(lahan_total):
        lahan.append(Lahan())

    lahan_total = 20
    lahan_tersedia = 20
    baris = 4

    hitung_lahan = int(lahan_total / baris)

    tepi = "|"
    for i in range(hitung_lahan - 1):
        for j in range(4):
            tepi += "-"
    tepi += "---|\n"

    v1 = kendaraan_masuk(1, "ad 1234 cd", 0, 3)
    v2 = kendaraan_masuk(3, "h  4321 ah", 1, 2)
    v3 = kendaraan_masuk(2, "ok 5768 ko", 2, 0)
    v4 = kendaraan_masuk(1, "bh 3324 hb", 3, 1)
    v5 = kendaraan_masuk(2, "ii 3421 jj", 2, 4)

    v1.set_waktu_masuk(1620561600)
    v2.set_waktu_masuk(1620570600)
    v3.set_waktu_masuk(1620577800)
    v4.set_waktu_masuk(1620576000)
    v5.set_waktu_masuk(1620586800)

def main():

    read_config()
    command = ""
    while command != "Q":
        tampilkan_lahan()
        print("Please Select An Option:\n"
              "P - Parkir\n"
              "E - Keluar\n"
              "V - Lihat Parkiran\n"
              "R - Tampilkan total bayar\n"
              "Q - Keluar Aplikasi\n")

        command = input(">")
        command_handler(command)

main()