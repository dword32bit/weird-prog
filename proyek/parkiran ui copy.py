import datetime
import time
import os
import numpy as np
arr = np.array([0,0,0,0,0],[0,0,0,0,0]) #Buat menjadi lahan parkiran jika terisi menjadi 1, jika tidak menjadi 0
parkiran = 10
parkir = []
log = {}
i = 0

def main():
    while True:
        render_ui()
        choice = input("Masukkan Pilihan anda: ")
        if choice == '1':
            park()
        elif choice == '2':
            exit_parking()
        elif choice == '3':
            render_parking_list()
        elif choice == '4':
            print(arr)
            exit_program()
        else:
            render_error()
            print("Inputan tidak Valid!")
            time.sleep(4)

def park():
    global parkiran, i
    if len(parkir) == parkiran:
        render_error()
        print("Parkiran Penuh!")
        time.sleep(2)
    else:
        kendaraan = input("Masukkan Plat Nomor kendaraan: ")
        kendaraan = kendaraan.upper()
        parkir.append(str(kendaraan))
        parkiran = parkiran - len(parkir)
        print("Kendaraan", kendaraan, "telah diparkir")
        log[i] = {'Plat': kendaraan}
        i += 1
        time.sleep(2)

def exit_parking():
    global i,parkiran
    render_parking_list()
    kendaraan = input("Masukkan Plat Nomor kendaraan: ")
    kendaraan = kendaraan.upper()
    if kendaraan not in parkir:
        render_error()
        print("Kendaraan tidak terparkir di parkiran")
        print("Plat Nomor kendaraan salah")
        time.sleep(2)
    else:
        biaya = get_cost(kendaraan)
        print('Biaya parkir = Rp.', biaya)
        parkir.remove(kendaraan)
        parkiran = parkiran - len(parkir)
        log[i] = {'Plat': kendaraan, 'Biaya': biaya}
        i += 1
        time.sleep(2)

def get_cost(name):
    enter = datetime.datetime.now()
    time.sleep(4)
    out = datetime.datetime.now()
    time_diff = out - enter
    days = time_diff.days
    days_to_hours = days * 24
    diff_btw_two_times = (time_diff.seconds) / 3600
    overall_hours = days_to_hours + diff_btw_two_times

    if overall_hours < 1:
        return 3000
    else:
        cost = overall_hours * 3000
        if cost > 5000:
            return 5000
        else:
            return cost

def render_ui():
    clear_screen()
    print("=========================================")
    print("          PARKIRAN ASCII UI")
    print("=========================================")
    print("Selamat datang di parkiran")
    print("parkiran yang tersedia:", parkiran)
    print("1. Parkir")
    print("2. Keluar")
    print("3. Lihat isi")
    print("4. Exit Program")

def render_error():
    print("=========================================")
    print("                  ERROR")
    print("=========================================")
    print("      ______                          ")
    print("     |  ____|                         ")
    print("     | |__    _ __  _ __  ___   _ __  ")
    print("     |  __|  | '__|| '__/ _ \ | '__| ")
    print("     | |____ | |   | | | (_) || |    ")
    print("     |______||_|   |_|  \___/ |_|    ")
    print("=========================================")

def render_exit():
    print("=========================================")
    print("             TERIMA KASIH")
    print("=========================================")
    print("Terimakasih untuk hari ini.....")

def render_parking_list():
    global i
    clear_screen()
    print("=========================================")
    print("           DAFTAR KENDARAAN")
    print("=========================================")
    print("Kendaraan yang terparkir:")
    print()
    for kendaraan in parkir:
        biaya = get_cost(kendaraan)
        print(" - [", kendaraan, "] ====> Rp.", biaya)
        log[i] = {'Plat': kendaraan, 'Biaya': biaya}
        i += 1
        print()
    print()
    input("Tekan Enter untuk kembali ke menu utama")

def exit_program():
    render_exit()
    time.sleep(3)
    clear_screen()
    for key, value in log.items():
        print('Data ke', key)
        print('Plat:', value['Plat'])
        print('Biaya:', value['Biaya'])
        print('Total:', value['Biaya'] * key)
        print()
    input("Tekan tombol apapun untuk mengakhiri ")
    exit()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

main()

