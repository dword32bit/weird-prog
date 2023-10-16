import datetime
import time
import os
a = datetime.datetime.now()
time.sleep(4)
b = datetime.datetime.now()

parkiran = int(10)
parkir=[]
def main():
    prog.menu()
    prog.prog()

class prog:
    global parkiran,parkir
    def menu():
        print("Selamat datang di parkiran")
        print("parkiran yang tersedia : ",parkiran - len(parkir))
        print("1. Parkir")
        print("2. Keluar")
        print("3. Lihat isi")
        print("4. Exit Program")
    def prog():
        pilihan=int(input("Masukkan Pilihan anda : "))
        if pilihan == 1:
            if parkiran == 0:
                Command.error()
                print("Parkiran Penuh !")
                main()
            else:
                m=input("Masukkan Plat Nomor kendaraan : ")
                parkir.append(str(m))
                print(parkir)
                print("parkiran yang tersedia : ",parkiran- len(parkir))
                time.sleep(2)
                os.system("cls")
                main()
        elif pilihan == 2:
            print(parkir)
            k=input("Masukkan Plat Nomor kendaraan : ")
            if k not in parkir:
                Command.error()
                print("Kendaraan tidak terparkir di parkiran")
                print("Plat Nomor kendaraan salah")
                Command.kembali()
            else:
                biaya = get_cost(k, a, b)
                print('Biaya parkir = Rp.',end='')
                print(biaya)
                parkir.remove(k)
                time.sleep(2)
                Command.kembali()
                os.system("cls")
        elif pilihan == 3:
            print(parkir)
            time.sleep(3)
            prog.prog()
        elif pilihan == 4:
            print("Terimakasih untuk hari ini.....")
            os.system("cls")
            exit()
        else:
            Command.error()
            print("Inputan tidak Valid ! ")
            prog.prog()   

class Command:
    def error():
            print("|==================================|")
            print("|  ______                          |")
            print("| |  ____|                         |")
            print("| | |__    _ __  _ __  ___   _ __  |")
            print("| |  __|  | '__|| '__|/ _ \ | '__| |")
            print("| | |____ | |   | |  | (_) || |    |")
            print("| |______||_|   |_|   \___/ |_|    |")
            print("|==================================|")
    def kembali():
        conf=input("Mau Kembali ke menu ? (y/n): ")
        if conf == "y":
            main()
        elif conf == "n":
            Command.error()
            Command.kembali()
            os.system('cls')
        else:
            Command.error()
            print("Inputan tidak valid !")
                                
def get_cost(name, enter, out):
    time = out - enter
    days = time.days
    days_to_hours = days * 24
    diff_btw_two_times = (time.seconds) / 3600
    overall_hours = days_to_hours + diff_btw_two_times

    if overall_hours < 1:
        return 3000, name
    else:
        cost = overall_hours * 3000
        if cost > 5000:
            return 5000, name
        else:
            return cost, name

while True:
    main()