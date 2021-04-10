import threading
from tkinter import *
from tkinter.ttk import Separator

from utils import *
from tkinter import messagebox, simpledialog

root = Tk()

companyName = StringVar(root, value='Название компании')
teamViewerPath = StringVar(root, value="TeamViewer.exe")

ip1name = StringVar(root, value='Шлюз')
ip1MainName = StringVar(root, value='Шлюз (' + str(get_def_gateway()) + ')')
ip1address = StringVar(root, value=get_def_gateway())

ip2name = StringVar(root, value='Интернет')
ip2address = StringVar(root, value='8.8.8.8')

ip3name1 = StringVar(root, value='Default')
ip3name2 = StringVar(root, value='Default')
ip3name3 = StringVar(root, value='Default')
ip3name4 = StringVar(root, value='Default')
ip3name5 = StringVar(root, value='Default')
ip3name6 = StringVar(root, value='Default')
ip3name7 = StringVar(root, value='Default')
ip3name8 = StringVar(root, value='Default')
ip3name9 = StringVar(root, value='Default')
ip3name10 = StringVar(root, value='Default')
ip3server1address = StringVar(root, value='000.000.000.000')
ip3server2address = StringVar(root, value='000.000.000.000')
ip3server3address = StringVar(root, value='000.000.000.000')
ip3server4address = StringVar(root, value='000.000.000.000')
ip3server5address = StringVar(root, value='000.000.000.000')
ip3server6address = StringVar(root, value='000.000.000.000')
ip3server7address = StringVar(root, value='000.000.000.000')
ip3server8address = StringVar(root, value='000.000.000.000')
ip3server9address = StringVar(root, value='000.000.000.000')
ip3server10address = StringVar(root, value='000.000.000.000')

statusVar = StringVar(root, value='')


def load_ip():
    configList = []
    if os.path.isfile('config.data') and os.path.getsize('config.data') > 0:
        with open('config.data', 'rb') as filehandle:
            configList = pickle.load(filehandle)
        filehandle.close()

        global ip1name
        ip1name.set(configList[0][0])

        global ip1address
        ip1address.set(configList[1][0])

        global ip2name
        ip2name.set(configList[0][1])

        global ip2address
        ip2address.set(configList[1][1])

        global ip3name1
        ip3name1.set(configList[0][2])

        global ip3name2
        ip3name2.set(configList[0][3])

        global ip3name3
        ip3name3.set(configList[0][4])

        global ip3name4
        ip3name4.set(configList[0][5])

        global ip3name5
        ip3name5.set(configList[0][6])

        global ip3name6
        ip3name6.set(configList[0][7])

        global ip3name7
        ip3name7.set(configList[0][8])

        global ip3name8
        ip3name8.set(configList[0][9])

        global ip3name9
        ip3name9.set(configList[0][10])

        global ip3name10
        ip3name10.set(configList[0][11])

        global companyName
        companyName.set(configList[0][12])

        global teamViewerPath
        teamViewerPath.set(configList[0][13])

        global ip3server1address
        ip3server1address.set(configList[2][0])

        global ip3server2address
        ip3server2address.set(configList[2][1])

        global ip3server3address
        ip3server3address.set(configList[2][2])

        global ip3server4address
        ip3server4address.set(configList[2][3])

        global ip3server5address
        ip3server5address.set(configList[2][4])

        global ip3server6address
        ip3server6address.set(configList[2][5])

        global ip3server7address
        ip3server7address.set(configList[2][6])

        global ip3server8address
        ip3server8address.set(configList[2][7])

        global ip3server9address
        ip3server9address.set(configList[2][8])

        global ip3server10address
        ip3server10address.set(configList[2][9])

def thread_fun_ping():
    x = threading.Thread(target=start_ping)
    x.start()

def start_ping():
    statusVar.set("Тестирую...")
    ip1 = ip1address.get()
    ip2 = ip2address.get()
    ip3 = [ip3server1address.get(), ip3server2address.get(), ip3server3address.get(), ip3server4address.get(),
           ip3server5address.get(), ip3server6address.get(), ip3server7address.get(), ip3server8address.get(),
           ip3server9address.get(), ip3server10address.get()]

    if ip1 != "000.000.000.000" and len(ip1) != 0:
        if ping_ip(ip1) == 0:
            app.ip1canvas.itemconfig(app.ip1Indicator, fill="lightgreen")
        elif ping_ip(ip1) == 1:
            app.ip1canvas.itemconfig(app.ip1Indicator, fill="red")
        else:
            app.ip1canvas.itemconfig(app.ip1Indicator, fill="yellow")
    else:
        app.ip1canvas.itemconfig(app.ip1Indicator, fill="")

    if ip2 != "000.000.000.000" and len(ip2) != 0:
        if ping_ip(ip2) == 0:
            app.ip2canvas.itemconfig(app.ip2Indicator, fill="lightgreen")
        elif ping_ip(ip2) == 1:
            app.ip2canvas.itemconfig(app.ip2Indicator, fill="red")
        else:
            app.ip2canvas.itemconfig(app.ip2Indicator, fill="yellow")
    else:
        app.ip2canvas.itemconfig(app.ip2Indicator, fill="")

    if ip3[0] != "000.000.000.000" and len(ip3[0]) != 0:
        if ping_ip(ip3[0]) == 0:
            app.ip3canvas1.itemconfig(app.ip3Indicator1, fill="lightgreen")
        elif ping_ip(ip3[0]) == 1:
            app.ip3canvas1.itemconfig(app.ip3Indicator1, fill="red")
        else:
            app.ip3canvas1.itemconfig(app.ip3Indicator1, fill="yellow")
    else:
        app.ip3canvas1.itemconfig(app.ip3Indicator1, fill="")

    if ip3[1] != "000.000.000.000" and len(ip3[1]) != 0:
        if ping_ip(ip3[1]) == 0:
            app.ip3canvas2.itemconfig(app.ip3Indicator2, fill="lightgreen")
        elif ping_ip(ip3[1]) == 1:
            app.ip3canvas2.itemconfig(app.ip3Indicator2, fill="red")
        else:
            app.ip3canvas2.itemconfig(app.ip3Indicator2, fill="yellow")
    else:
        app.ip3canvas2.itemconfig(app.ip3Indicator2, fill="")

    if ip3[2] != "000.000.000.000" and len(ip3[2]) != 0:
        if ping_ip(ip3[2]) == 0:
            app.ip3canvas3.itemconfig(app.ip3Indicator3, fill="lightgreen")
        elif ping_ip(ip3[2]) == 1:
            app.ip3canvas3.itemconfig(app.ip3Indicator3, fill="red")
        else:
            app.ip3canvas3.itemconfig(app.ip3Indicator3, fill="yellow")
    else:
        app.ip3canvas3.itemconfig(app.ip3Indicator3, fill="")

    if ip3[3] != "000.000.000.000" and len(ip3[3]) != 0:
        if ping_ip(ip3[3]) == 0:
            app.ip3canvas4.itemconfig(app.ip3Indicator4, fill="lightgreen")
        elif ping_ip(ip3[3]) == 1:
            app.ip3canvas4.itemconfig(app.ip3Indicator4, fill="red")
        else:
            app.ip3canvas4.itemconfig(app.ip3Indicator4, fill="yellow")
    else:
        app.ip3canvas4.itemconfig(app.ip3Indicator4, fill="")

    if ip3[4] != "000.000.000.000" and len(ip3[4]) != 0:
        if ping_ip(ip3[4]) == 0:
            app.ip3canvas5.itemconfig(app.ip3Indicator5, fill="lightgreen")
        elif ping_ip(ip3[4]) == 1:
            app.ip3canvas5.itemconfig(app.ip3Indicator5, fill="red")
        else:
            app.ip3canvas5.itemconfig(app.ip3Indicator5, fill="yellow")
    else:
        app.ip3canvas5.itemconfig(app.ip3Indicator5, fill="")

    if ip3[5] != "000.000.000.000" and len(ip3[5]) != 0:
        if ping_ip(ip3[5]) == 0:
            app.ip3canvas6.itemconfig(app.ip3Indicator6, fill="lightgreen")
        elif ping_ip(ip3[5]) == 1:
            app.ip3canvas6.itemconfig(app.ip3Indicator6, fill="red")
        else:
            app.ip3canvas6.itemconfig(app.ip3Indicator6, fill="yellow")
    else:
        app.ip3canvas6.itemconfig(app.ip3Indicator6, fill="")

    if ip3[6] != "000.000.000.000" and len(ip3[6]) != 0:
        if ping_ip(ip3[6]) == 0:
            app.ip3canvas7.itemconfig(app.ip3Indicator7, fill="lightgreen")
        elif ping_ip(ip3[6]) == 1:
            app.ip3canvas7.itemconfig(app.ip3Indicator7, fill="red")
        else:
            app.ip3canvas7.itemconfig(app.ip3Indicator7, fill="yellow")
    else:
        app.ip3canvas7.itemconfig(app.ip3Indicator7, fill="")

    if ip3[7] != "000.000.000.000" and len(ip3[7]) != 0:
        if ping_ip(ip3[7]) == 0:
            app.ip3canvas8.itemconfig(app.ip3Indicator8, fill="lightgreen")
        elif ping_ip(ip3[7]) == 1:
            app.ip3canvas8.itemconfig(app.ip3Indicator8, fill="red")
        else:
            app.ip3canvas8.itemconfig(app.ip3Indicator8, fill="yellow")
    else:
        app.ip3canvas8.itemconfig(app.ip3Indicator8, fill="")

    if ip3[8] != "000.000.000.000" and len(ip3[8]) != 0:
        if ping_ip(ip3[8]) == 0:
            app.ip3canvas9.itemconfig(app.ip3Indicator9, fill="lightgreen")
        elif ping_ip(ip3[8]) == 1:
            app.ip3canvas9.itemconfig(app.ip3Indicator9, fill="red")
        else:
            app.ip3canvas9.itemconfig(app.ip3Indicator9, fill="yellow")
    else:
        app.ip3canvas9.itemconfig(app.ip3Indicator9, fill="")

    if ip3[9] != "000.000.000.000" and len(ip3[9]) != 0:
        if ping_ip(ip3[9]) == 0:
            app.ip3canvas10.itemconfig(app.ip3Indicator10, fill="lightgreen")
        elif ping_ip(ip3[9]) == 1:
            app.ip3canvas10.itemconfig(app.ip3Indicator10, fill="red")
        else:
            app.ip3canvas10.itemconfig(app.ip3Indicator10, fill="yellow")
    else:
        app.ip3canvas10.itemconfig(app.ip3Indicator10, fill="")

    statusVar.set("Тест завершен")




def conf_ping():
    if config_login():
        inputDialog = MyDialog(root)
        root.wait_window(inputDialog.top)
        load_ip()


def config_login():
    res = False
    root_password = ""
    real_password = []
    if os.path.isfile('passwd.key') and os.path.getsize('passwd.key') > 0:
        with open('passwd.key', 'rb') as filehandle:
            real_password = pickle.load(filehandle)
        filehandle.close()
        root_password = simpledialog.askstring("Пароль", "Введите пароль администратора:", show='*')
        if not root_password is None:
            root_password = hashlib.pbkdf2_hmac('sha256', root_password.encode('utf-8'), real_password[0], 100000)
            if root_password == real_password[1]:
                res = True
            else:
                messagebox.showwarning("Ошибка", "Неверный пароль")
    else:
        messagebox.showwarning("Ошибка", "пароль не задан")
    return res


class MyDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.titleLab = Label(top, text='Введите адреса ip')
        self.titleLab.grid(row=0, column=0, columnspan=8, ipadx=10, sticky=W + E)

        self.ip1NameLab = Label(top, text='1. Имя:')
        self.ip1NameLab.grid(row=1, column=0, ipadx=10, pady=10, sticky=W)

        self.ip1NameEntry = Entry(top, textvariable=ip1name)
        self.ip1NameEntry.grid(row=1, column=1, ipadx=10, pady=10, sticky=W)

        self.ip1AddressLab = Label(top, text='Адрес ip:')
        self.ip1AddressLab.grid(row=1, column=2, ipadx=10, pady=10, sticky=W)

        self.ip1AddressEntry = Entry(top, textvariable=ip1address)
        self.ip1AddressEntry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        self.ip2NameLab = Label(top, text='2. Имя:')
        self.ip2NameLab.grid(row=2, column=0, ipadx=10, pady=10, sticky=W)

        self.ip2NameEntry = Entry(top, textvariable=ip2name)
        self.ip2NameEntry.grid(row=2, column=1, ipadx=10, pady=10, sticky=W)

        self.ip2AddressLab = Label(top, text='Адрес ip:')
        self.ip2AddressLab.grid(row=2, column=2, ipadx=10, pady=10, sticky=W)

        self.ip2AddressEntry = Entry(top, textvariable=ip2address)
        self.ip2AddressEntry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        self.ip3server1NameLab = Label(top, text='3. 1.Имя:')
        self.ip3server1NameLab.grid(row=3, column=0, ipadx=10, pady=10, sticky=W)

        self.ip3Name1Entry = Entry(top, textvariable=ip3name1)
        self.ip3Name1Entry.grid(row=3, column=1, ipadx=10, pady=10, sticky=W)

        self.ip3server1AddressLab = Label(top, text='Адрес ip:')
        self.ip3server1AddressLab.grid(row=3, column=2, ipadx=10, pady=10, sticky=W)

        self.ip3server1AddressEntry = Entry(top, textvariable=ip3server1address)
        self.ip3server1AddressEntry.grid(row=3, column=3, padx=10, pady=10, sticky=W)



        self.ip3server2NameLab = Label(top, text='2.Имя:')
        self.ip3server2NameLab.grid(row=3, column=4, ipadx=10, pady=10, sticky=W)

        self.ip3Name2Entry = Entry(top, textvariable=ip3name2)
        self.ip3Name2Entry.grid(row=3, column=5, ipadx=10, pady=10, sticky=W)

        self.ip3server2AddressLab = Label(top, text='Адрес ip:')
        self.ip3server2AddressLab.grid(row=3, column=6, ipadx=10, pady=10, sticky=W)

        self.ip3server2AddressEntry = Entry(top, textvariable=ip3server2address)
        self.ip3server2AddressEntry.grid(row=3, column=7, padx=10, pady=10, sticky=W)



        self.ip3server3NameLab = Label(top, text='3.Имя:')
        self.ip3server3NameLab.grid(row=4, column=0, ipadx=10, pady=10, sticky=W)

        self.ip3Name3Entry = Entry(top, textvariable=ip3name3)
        self.ip3Name3Entry.grid(row=4, column=1, ipadx=10, pady=10, sticky=W)

        self.ip3server3AddressLab = Label(top, text='Адрес ip:')
        self.ip3server3AddressLab.grid(row=4, column=2, ipadx=10, pady=10, sticky=W)

        self.ip3server3AddressEntry = Entry(top, textvariable=ip3server3address)
        self.ip3server3AddressEntry.grid(row=4, column=3, padx=10, pady=10, sticky=W)



        self.ip3server4NameLab = Label(top, text='4.Имя:')
        self.ip3server4NameLab.grid(row=4, column=4, ipadx=10, pady=10, sticky=W)

        self.ip3Name4Entry = Entry(top, textvariable=ip3name4)
        self.ip3Name4Entry.grid(row=4, column=5, ipadx=10, pady=10, sticky=W)

        self.ip3server4AddressLab = Label(top, text='Адрес ip:')
        self.ip3server4AddressLab.grid(row=4, column=6, ipadx=10, pady=10, sticky=W)

        self.ip3server4AddressEntry = Entry(top, textvariable=ip3server4address)
        self.ip3server4AddressEntry.grid(row=4, column=7, padx=10, pady=10, sticky=W)



        self.ip3server5NameLab = Label(top, text='5.Имя:')
        self.ip3server5NameLab.grid(row=5, column=0, ipadx=10, pady=10, sticky=W)

        self.ip3Name5Entry = Entry(top, textvariable=ip3name5)
        self.ip3Name5Entry.grid(row=5, column=1, ipadx=10, pady=10, sticky=W)

        self.ip3server5AddressLab = Label(top, text='Адрес ip:')
        self.ip3server5AddressLab.grid(row=5, column=2, ipadx=10, pady=10, sticky=W)

        self.ip3server5AddressEntry = Entry(top, textvariable=ip3server5address)
        self.ip3server5AddressEntry.grid(row=5, column=3, padx=10, pady=10, sticky=W)



        self.ip3server6NameLab = Label(top, text='6.Имя:')
        self.ip3server6NameLab.grid(row=5, column=4, ipadx=10, pady=10, sticky=W)

        self.ip3Name6Entry = Entry(top, textvariable=ip3name4)
        self.ip3Name6Entry.grid(row=5, column=5, ipadx=10, pady=10, sticky=W)

        self.ip3server6AddressLab = Label(top, text='Адрес ip:')
        self.ip3server6AddressLab.grid(row=5, column=6, ipadx=10, pady=10, sticky=W)

        self.ip3server6AddressEntry = Entry(top, textvariable=ip3server6address)
        self.ip3server6AddressEntry.grid(row=5, column=7, padx=10, pady=10, sticky=W)



        self.ip3server7NameLab = Label(top, text='7.Имя:')
        self.ip3server7NameLab.grid(row=6, column=0, ipadx=10, pady=10, sticky=W)

        self.ip3Name7Entry = Entry(top, textvariable=ip3name7)
        self.ip3Name7Entry.grid(row=6, column=1, ipadx=10, pady=10, sticky=W)

        self.ip3server7AddressLab = Label(top, text='Адрес ip:')
        self.ip3server7AddressLab.grid(row=6, column=2, ipadx=10, pady=10, sticky=W)

        self.ip3server7AddressEntry = Entry(top, textvariable=ip3server7address)
        self.ip3server7AddressEntry.grid(row=6, column=3, padx=10, pady=10, sticky=W)



        self.ip3server8NameLab = Label(top, text='8.Имя:')
        self.ip3server8NameLab.grid(row=6, column=4, ipadx=10, pady=10, sticky=W)

        self.ip3Name8Entry = Entry(top, textvariable=ip3name8)
        self.ip3Name8Entry.grid(row=6, column=5, ipadx=10, pady=10, sticky=W)

        self.ip3server8AddressLab = Label(top, text='Адрес ip:')
        self.ip3server8AddressLab.grid(row=6, column=6, ipadx=10, pady=10, sticky=W)

        self.ip3server8AddressEntry = Entry(top, textvariable=ip3server8address)
        self.ip3server8AddressEntry.grid(row=6, column=7, padx=10, pady=10, sticky=W)



        self.ip3server9NameLab = Label(top, text='9.Имя:')
        self.ip3server9NameLab.grid(row=7, column=0, ipadx=10, pady=10, sticky=W)

        self.ip3Name9Entry = Entry(top, textvariable=ip3name9)
        self.ip3Name9Entry.grid(row=7, column=1, ipadx=10, pady=10, sticky=W)

        self.ip3server9AddressLab = Label(top, text='Адрес ip:')
        self.ip3server9AddressLab.grid(row=7, column=2, ipadx=10, pady=10, sticky=W)

        self.ip3server9AddressEntry = Entry(top, textvariable=ip3server9address)
        self.ip3server9AddressEntry.grid(row=7, column=3, padx=10, pady=10, sticky=W)



        self.ip3server10NameLab = Label(top, text='10.Имя:')
        self.ip3server10NameLab.grid(row=7, column=4, ipadx=10, pady=10, sticky=W)

        self.ip3Name10Entry = Entry(top, textvariable=ip3name10)
        self.ip3Name10Entry.grid(row=7, column=5, ipadx=10, pady=10, sticky=W)

        self.ip3server10AddressLab = Label(top, text='Адрес ip:')
        self.ip3server10AddressLab.grid(row=7, column=6, ipadx=10, pady=10, sticky=W)

        self.ip3server10AddressEntry = Entry(top, textvariable=ip3server10address)
        self.ip3server10AddressEntry.grid(row=7, column=7, padx=10, pady=10, sticky=W)



        self.companyLab = Label(top, text='4. Название компании:')
        self.companyLab.grid(row=8, column=0, ipadx=10, pady=10, sticky=W)

        self.companyEntry = Entry(top, textvariable=companyName)
        self.companyEntry.grid(row=8, column=1, padx=10, pady=10, sticky=W)

        self.teamViewerButton = Button(top, text='выбрать путь', command=self.get_path)
        self.teamViewerButton.grid(row=9, column=0, padx=10, pady=10,  sticky=W)

        self.teamViewerEntry = Entry(top, textvariable=teamViewerPath)
        self.teamViewerEntry.grid(row=9, column=1, ipadx=10, pady=10, sticky=W)

        self.mySubmitButton = Button(top, text='Save', command=self.save)
        self.mySubmitButton.grid(row=10, column=0, columnspan=8, padx=10, pady=10)

    def entry_match(self):
        res = True
        ipAdresses = [self.ip3server1AddressEntry.get(), self.ip3server2AddressEntry.get(),
                      self.ip3server3AddressEntry.get(),
                      self.ip3server4AddressEntry.get(), self.ip3server5AddressEntry.get(),
                      self.ip3server6AddressEntry.get(),
                      self.ip3server7AddressEntry.get(), self.ip3server8AddressEntry.get(),
                      self.ip3server9AddressEntry.get(),
                      self.ip3server10AddressEntry.get(), self.ip1AddressEntry.get(),
                      self.ip2AddressEntry.get()]
        for ip in ipAdresses:
            if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
                res = False
        return res

    def get_path(self):
        global teamViewerPath
        path = get_path()
        if not path is None:
            teamViewerPath.set(path)

    def save(self):
        if not self.entry_match():
            messagebox.showwarning("Ошибка", "Адрес IP введен не верно")
        else:
            self.ipNameList = [self.ip1NameEntry.get(), self.ip2NameEntry.get(), self.ip3Name1Entry.get(),
                               self.ip3Name2Entry.get(), self.ip3Name3Entry.get(), self.ip3Name4Entry.get(),
                               self.ip3Name5Entry.get(), self.ip3Name6Entry.get(), self.ip3Name7Entry.get(),
                               self.ip3Name8Entry.get(), self.ip3Name9Entry.get(), self.ip3Name10Entry.get(),
                               self.companyEntry.get(), self.teamViewerEntry.get()]
            self.ipAdressList = [self.ip1AddressEntry.get(), self.ip2AddressEntry.get()]
            self.ipServerAdresses = [self.ip3server1AddressEntry.get(), self.ip3server2AddressEntry.get(),
                                     self.ip3server3AddressEntry.get(),
                                     self.ip3server4AddressEntry.get(), self.ip3server5AddressEntry.get(),
                                     self.ip3server6AddressEntry.get(),
                                     self.ip3server7AddressEntry.get(), self.ip3server8AddressEntry.get(),
                                     self.ip3server9AddressEntry.get(),
                                     self.ip3server10AddressEntry.get()]
            self.configList = [self.ipNameList, self.ipAdressList, self.ipServerAdresses]
            with open('config.data', 'wb') as filehandle:
                pickle.dump(self.configList, filehandle)
            filehandle.close()
            self.top.destroy()

    def on_closing(self):
        self.top.destroy()

def run_remote_access():
    run_program(teamViewerPath.get())


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("netboks tester")

        self.companyLab = Label(root, textvariable=companyName)
        self.companyLab.grid(row=0, column=0, columnspan=5, ipadx=10)

        self.delimiter1 = Separator(root, orient='horizontal')
        self.delimiter1.grid(row=1, column=0, columnspan=5, ipadx=10, sticky=W + E)

        self.btnStartIPTest = Button(root, text="Тест", command=thread_fun_ping)
        self.btnStartIPTest.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.statusLab = Label(root, textvariable=statusVar)
        self.statusLab.grid(row=3, column=0, ipadx=10, sticky=W)

        self.ip1NameLab = Label(root, textvariable=ip1MainName)
        self.ip1NameLab.grid(row=2, column=1, ipadx=10, sticky=W)

        self.ip2NameLab = Label(root, textvariable=ip2name)
        self.ip2NameLab.grid(row=3, column=1, ipadx=10, sticky=W)

        self.ip3Name1Lab = Label(root, textvariable=ip3name1)
        self.ip3Name1Lab.grid(row=4, column=1, ipadx=10, sticky=W)

        self.ip3canvas1 = Canvas(root, width=40, height=40)
        self.ip3canvas1.grid(row=4, column=2, ipadx=10, sticky=W)
        self.ip3Indicator1 = self.ip3canvas1.create_oval(14, 14, 28, 28)

        self.ip3Name2Lab = Label(root, textvariable=ip3name2)
        self.ip3Name2Lab.grid(row=4, column=3, ipadx=10, sticky=W)

        self.ip3canvas2 = Canvas(root, width=40, height=40)
        self.ip3canvas2.grid(row=4, column=4, ipadx=10, sticky=W)
        self.ip3Indicator2 = self.ip3canvas2.create_oval(14, 14, 28, 28)


        self.ip3Name3Lab = Label(root, textvariable=ip3name3)
        self.ip3Name3Lab.grid(row=5, column=1, ipadx=10, sticky=W)

        self.ip3canvas3 = Canvas(root, width=40, height=40)
        self.ip3canvas3.grid(row=5, column=2, ipadx=10, sticky=W)
        self.ip3Indicator3 = self.ip3canvas3.create_oval(14, 14, 28, 28)

        self.ip3Name4Lab = Label(root, textvariable=ip3name4)
        self.ip3Name4Lab.grid(row=5, column=3, ipadx=10, sticky=W)

        self.ip3canvas4 = Canvas(root, width=40, height=40)
        self.ip3canvas4.grid(row=5, column=4, ipadx=10, sticky=W)
        self.ip3Indicator4 = self.ip3canvas4.create_oval(14, 14, 28, 28)



        self.ip3Name5Lab = Label(root, textvariable=ip3name5)
        self.ip3Name5Lab.grid(row=6, column=1, ipadx=10, sticky=W)

        self.ip3canvas5 = Canvas(root, width=40, height=40)
        self.ip3canvas5.grid(row=6, column=2, ipadx=10, sticky=W)
        self.ip3Indicator5 = self.ip3canvas5.create_oval(14, 14, 28, 28)

        self.ip3Name6Lab = Label(root, textvariable=ip3name6)
        self.ip3Name6Lab.grid(row=6, column=3, ipadx=10, sticky=W)

        self.ip3canvas6 = Canvas(root, width=40, height=40)
        self.ip3canvas6.grid(row=6, column=4, ipadx=10, sticky=W)
        self.ip3Indicator6 = self.ip3canvas6.create_oval(14, 14, 28, 28)



        self.ip3Name7Lab = Label(root, textvariable=ip3name7)
        self.ip3Name7Lab.grid(row=7, column=1, ipadx=10, sticky=W)

        self.ip3canvas7 = Canvas(root, width=40, height=40)
        self.ip3canvas7.grid(row=7, column=2, ipadx=10, sticky=W)
        self.ip3Indicator7 = self.ip3canvas7.create_oval(14, 14, 28, 28)

        self.ip3Name8Lab = Label(root, textvariable=ip3name8)
        self.ip3Name8Lab.grid(row=7, column=3, ipadx=10, sticky=W)

        self.ip3canvas8 = Canvas(root, width=40, height=40)
        self.ip3canvas8.grid(row=7, column=4, ipadx=10, sticky=W)
        self.ip3Indicator8 = self.ip3canvas8.create_oval(14, 14, 28, 28)



        self.ip3Name9Lab = Label(root, textvariable=ip3name9)
        self.ip3Name9Lab.grid(row=8, column=1, ipadx=10, sticky=W)

        self.ip3canvas9 = Canvas(root, width=40, height=40)
        self.ip3canvas9.grid(row=8, column=2, ipadx=10, sticky=W)
        self.ip3Indicator9 = self.ip3canvas9.create_oval(14, 14, 28, 28)

        self.ip3Name10Lab = Label(root, textvariable=ip3name10)
        self.ip3Name10Lab.grid(row=8, column=3, ipadx=10, sticky=W)

        self.ip3canvas10 = Canvas(root, width=40, height=40)
        self.ip3canvas10.grid(row=8, column=4, ipadx=10, sticky=W)
        self.ip3Indicator10 = self.ip3canvas10.create_oval(14, 14, 28, 28)



        self.btnConfigIPTest = Button(root, text="Конфигурация", command=conf_ping)
        self.btnConfigIPTest.grid(row=9, column=0, padx=10, pady=10, sticky=W)

        self.delimiter2 = Separator(root, orient='horizontal')
        self.delimiter2.grid(row=10, column=0, columnspan=5, ipadx=10, sticky=W + E)

        self.btnTeamViewerRun = Button(root, text="Удаленный доступ", command=run_remote_access)
        self.btnTeamViewerRun.grid(row=11, column=0, padx=10, pady=10, sticky=W)

        self.ip1canvas = Canvas(root, width=40, height=40)
        self.ip1canvas.grid(row=2, column=2, ipadx=10, sticky=W)
        self.ip1Indicator = self.ip1canvas.create_oval(14, 14, 28, 28)

        self.ip2canvas = Canvas(root, width=40, height=40)
        self.ip2canvas.grid(row=3, column=2, ipadx=10, sticky=W)
        self.ip2Indicator = self.ip2canvas.create_oval(14, 14, 28, 28)


def main():
    load_ip()
    global app
    app = Main(root)
    root.mainloop()


if __name__ == "__main__":
    main()
