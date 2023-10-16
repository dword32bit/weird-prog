from tkinter import *
from tkinter.font import BOLD
from tkinter.messagebox import *


class UIandFunction:
    def __init__(self, root, Basecolor):
        self.sv = StringVar()
        self.sv2 = StringVar()

        # tampilan frame atas
        self.frameTop(root, Basecolor)

        # tampilan frame bawah
        self.frameBottom(root, Basecolor)

        # event entry waktu keluar
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv, 1))

        # event entry waktu masuk
        self.sv2.trace("w", lambda name, index, mode, sv2=self.sv2: self.callback(sv2, 2))

        # event button simpan data
        self.btn_save.bind("<Button>", lambda e: self.insertData(self.frametable, self.data_list))

        # event button search data
        self.btn_search.bind("<Button>", lambda e: self.searchTwoD(str(self.s_no_plat.get()), self.data_list))

    # function for UI top frame
    def frameTop(self, root, Basecolor):
        frametop = Frame(root, bg=Basecolor)
        frameleft = Frame(frametop, bg=Basecolor)
        lb_title = Label(frameleft, text="APLIKASI PARKIR KELOMPOK 3", bg=Basecolor)
        lb_title.config(font=("Helvetica", 10, BOLD))
        lb_title.pack()
        Label(frameleft, text="Cari NoPol", bg=Basecolor).place(x=30, y=40)
        self.s_no_plat = s_no_plat = Entry(frameleft)
        s_no_plat.place(x=115, y=40)
        self.btn_search = btn_search = Button(frameleft, text="Cari", activebackground="pink", activeforeground="blue")
        btn_search.place(x=280, y=40)
        Label(frameleft, text="No Plat Polisi", bg=Basecolor).place(x=30, y=90)
        Label(frameleft, text="Waktu Masuk", bg=Basecolor).place(x=30, y=130)
        Label(frameleft, text="Waktu Keluar", bg=Basecolor).place(x=30, y=170)
        Label(frameleft, text="Biaya", bg=Basecolor).place(x=30, y=210)
        self.btn_save = btn_save = Button(frameleft, text="Simpan", activebackground="pink", activeforeground="blue")
        btn_save.place(x=280, y=208)
        self.i_no_plat = i_no_plat = Entry(frameleft)
        i_no_plat.place(x=125, y=90)
        self.i_wm = i_wm = Entry(frameleft, textvariable=self.sv2)
        i_wm.insert(END, '00:00')
        i_wm.place(x=125, y=130)
        self.i_ws = i_ws = Entry(frameleft, textvariable=self.sv)
        i_ws.insert(END, '01:00')
        i_ws.place(x=125, y=170)
        self.i_biaya = i_biaya = Entry(frameleft)
        i_biaya.insert(END, '2000')
        i_biaya.place(x=125, y=210)
        lb_table1 = Label(frameleft, text="List Pelanggan Urut Terakhir Keluar", bg=Basecolor, fg="blue")
        lb_table1.config(font=("Helvetica", 12, BOLD))
        lb_table1.place(x=30, y=255)
        frameleft.pack(fill='both', side='left', expand='True')
        frameright = Frame(frametop, bg=Basecolor)
        Label(frameright, text="Pembatas Tak Terlihat", bg=Basecolor, fg=Basecolor).pack()
        lb_title_bayar = Label(frameright, text="Biaya Parkir Per Jam", fg="red", bg=Basecolor)
        lb_title_bayar.config(font=("Helvetica", 12, BOLD))
        lb_title_bayar.place(x=0, y=70)
        lb_bayar = Label(frameright, text="Rp 2.000", fg="red", bg=Basecolor)
        lb_bayar.config(font=("Helvetica", 42, BOLD))
        lb_bayar.place(x=0, y=90)
        lb_table2 = Label(frameright, text="List Pelanggan Banyak Bayar", bg=Basecolor, fg="blue")
        lb_table2.config(font=("Helvetica", 12, BOLD))
        lb_table2.place(x=0, y=255)
        frameright.pack(fill='both', side='right', expand='True')
        frametop.pack(fill='both', side='top', expand='True')

    # function for UI bottom frame
    def frameBottom(self, root, Basecolor):
        data_list = []
        framebottom = Frame(root, bg=Basecolor)
        lbframe_left = LabelFrame(framebottom, bd=8)
        self.tableGrid(1, lbframe_left, data_list)
        lbframe_left.pack(side='left')
        lbframe_right = LabelFrame(framebottom, bd=8)
        self.tableGrid(2, lbframe_right, data_list)
        lbframe_right.pack(side='right')
        framebottom.pack(fill='both', side='bottom')
        self.frametable = [lbframe_left, lbframe_right]
        self.data_list = data_list

    # function table grid
    def tableGrid(self, indikator, frame, data_list):
        if indikator == 1:
            data_list_update = self.Sort(data_list, 2)
        else:
            data_list_update = self.Sort(data_list, 3)
        title = [['No Plat Polisi', 'Masuk', 'Keluar', 'Biaya']]
        data_list_update = title + data_list_update
        for i in range(len(data_list_update)):
            for j in range(len(data_list_update[0])):
                e = Entry(frame, width=12, fg='blue', font=('Arial', 10))
                e.grid(row=i, column=j)
                e.insert(END, data_list_update[i][j])

    # function for sort
    def Sort(self, sub_li, index):
        return sorted(sub_li, key=lambda x: x[index], reverse=True)

    # function insert
    def insertData(self, frametable, data_list):
        if str(self.i_no_plat.get()) != '':
            if len(data_list) < 1:
                data_list.append(
                    [str(self.i_no_plat.get()), str(self.i_wm.get()), str(self.i_ws.get()), int(self.i_biaya.get())])
                showinfo(title='Insert Success', message='Data berhasil dimasukkan.')
            else:
                no_data_same = True
                for i in range(len(data_list)):
                    if data_list[i][0] == str(self.i_no_plat.get()):
                        no_data_same = False
                        break
                if no_data_same:
                    data_list.append(
                        [str(self.i_no_plat.get()), str(self.i_wm.get()), str(self.i_ws.get()),
                        int(self.i_biaya.get())])
                    showinfo(title='Insert Success', message='Data berhasil dimasukkan.')
                else:
                    showerror(title='Insert gagal', message='No Plat Polisi tersebut sudah terdapat di dalam data list')
        else:
            showerror(title='Insert gagal', message='No Plat Polisi tersebut tidak boleh kosong')
        for i in range(len(frametable)):
            self.tableGrid(i + 1, frametable[i], data_list)

    # callback from entry
    def callback(self, sv, indicator):
        data = str(sv.get())
        if len(data) == 5:
            if indicator == 1:
                jam = int(data[:2]) - int(str(self.i_wm.get())[:2])
            else:
                jam = int(str(self.i_ws.get())[:2]) - int(data[:2])
            biaya = jam * 2000
            self.i_biaya.delete(0, END)
            self.i_biaya.insert(0, str(biaya))

    # function search
    def searchTwoD(self, string, list, message=''):
        for i in range(len(list)):
            if list[i][0] == string:
                message = ' Plat NoPol: ' + list[i][0] + ' \n Masuk: ' + list[i][1] + ' \n Keluar: ' + list[i][
                    2] + ' \n Biaya: ' + str(list[i][3])
                self.i_no_plat.delete(0, END)
                self.i_no_plat.insert(END, list[i][0])
                self.i_wm.delete(0, END)
                self.i_wm.insert(END, list[i][1])
                self.i_ws.delete(0, END)
                self.i_ws.insert(END, list[i][2])
                self.i_biaya.delete(0, END)
                self.i_biaya.insert(END, list[i][3])
                break
        if message != '':
            showinfo(title="Data Ditemukan", message=message)
        else:
            message = 'Data yang anda cari tidak ada!'
            showerror(title='Not Found', message=message)


if __name__ == "__main__":
    Basecolor = '#%02x%02x%02x' % (64, 204, 208)
    root = Tk()
    root.geometry("740x600")
    root.resizable(False, False)
    root.title('Parking APPS')
    # main ui dan beberapa fungsinya
    UIandFunction(root, Basecolor)
    root.mainloop()