import hashlib
import os
import platform
import re
import subprocess
from tkinter import filedialog

import netifaces
import pickle


def ping_ip(ip):
    res = 0
    current_os = platform.system().lower()
    parameter = "-c"
    if current_os == "windows":
        parameter = "-n"

    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    command = ['ping', parameter, '4', ip]
    process = subprocess.Popen(command, startupinfo=si, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    percentage = 0

    f = process.stdout.read().decode('ISO-8859-1').split()
    for x in f:
        if re.match(r".*%.*", x):
            strArr = []
            strArr[:0] = x
            strArr = strArr[1:-1]
            listToStr = ''.join(map(str, strArr))
            percentage = int(listToStr)
    if percentage == 0:
        res = 0  # 0% loss
    elif percentage == 100:
        res = 1  # 100% loss
    else:
        res = 2  # partial loss
    return res



def get_def_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    return default_gateway


def make_password(password):
    salt = os.urandom(32)  # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    passwd = [salt, key]
    with open('passwd.key', 'wb') as filehandle:
        pickle.dump(passwd, filehandle)
    filehandle.close()


def run_program(path):
    command = [path]
    subprocess.Popen(command)


def get_path():
    path = filedialog.askopenfilename(title='Please select an runable file .exe')
    return path

# E:\Python\anaconda3\Scripts\pyinstaller.exe --onefile --windowed main_interface.py
