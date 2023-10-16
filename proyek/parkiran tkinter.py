import datetime
import time
import tkinter as tk
from tkinter import messagebox

parkiran = 10
parkir = []

def main():
    global biaya

    def masuk():
        if len(parkir) == parkiran:
            messagebox.showerror("Error", "Parkiran Penuh!")
        else:
            kendaraan = ui.kendaraan_entry.get(kendaraan)
            parkir.append(kendaraan)
            update_parking_status()
            messagebox.showinfo("Parkir", f"Kendaraan {kendaraan} telah diparkir.")

    def keluar():
        kendaraan = ui.kendaraan_entry.get(kendaraan)
        if kendaraan not in parkir:
            messagebox.showerror("Error", "Kendaraan tidak terparkir di parkiran atau Plat Nomor kendaraan salah")
        else:
            biaya = get_cost(kendaraan)
            messagebox.showinfo("Biaya Parkir", f"Biaya parkir = Rp. {biaya}")
            parkir.remove(kendaraan)
            update_parking_status()

    def list_parkiran():
        parking_list = '\n'.join(f"- {kendaraan}: Rp. {get_cost(kendaraan)}" for kendaraan in parkir)
        messagebox.showinfo("Daftar Kendaraan", f"Kendaraan yang terparkir:\n\n{parking_list}")

    def update_parking_status():
        ui.parkiran_status_label.config(text=f"Parkiran Tersedia: {parkiran - len(parkir)}")

    def ui():
        window = tk.Tk()
        window.title("Parkiran")
        window.geometry("1366x768")

        parkiran_status_label = tk.Label(window, text=f"Parkiran Tersedia: {parkiran - len(parkir)}")
        parkiran_status_label.pack()

        kendaraan_label = tk.Label(window, text="Masukkan Plat Nomor kendaraan:")
        kendaraan_label.pack()

        kendaraan_entry = tk.Entry(window)
        kendaraan_entry.pack()

        park_button = tk.Button(window, text="Parkir", command=masuk)
        park_button.pack()

        exit_button = tk.Button(window, text="Keluar", command=keluar)
        exit_button.pack()

        list_button = tk.Button(window, text="Lihat isi", command=list_parkiran)
        list_button.pack()

        window.mainloop()

    ui()

def get_cost(name):
    enter = datetime.datetime.now()
    out = datetime.datetime.now()
    time = out - enter
    days = time.days
    days_to_hours = days * 24
    diff_btw_two_times = (time.seconds) / 3600
    overall_hours = days_to_hours + diff_btw_two_times

    if overall_hours < 1:
        return 3000
    else:
        cost = overall_hours * 3000
        if cost > 5000:
            return 5000
        else:
            return cost

main()
