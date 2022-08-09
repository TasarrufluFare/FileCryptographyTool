import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import font
import encrypter
import decrypter
import subprocess


form = tk.Tk(screenName="File Encrypter")
form.title("File Cryptography")
form.geometry("308x120")
form.minsize(308, 120)
form.maxsize(308, 120)
form.iconphoto(False, tk.PhotoImage(file='icon.png'))
form.configure(background="#301024")
myFont1 = font.Font(family='Courier', size=14, weight='bold')
myFont2 = font.Font(family='Courier', size=10, weight='bold')

secilen = tk.StringVar()
checkbox_secilen = tk.IntVar()


def confirm():
    mod = secilen.get()
    mod_checkbox = checkbox_secilen.get()

    if mod == "Value 2":
        filename = fd.askopenfilename(filetypes=[("All files", "*")])
        if filename != "":
            print("Encrypt File")
            encrypter.encrypter_method(filename)
            print(filename)
            subprocess.Popen('explorer "Operations"')
            if mod_checkbox == 1:
                os.remove(filename)

    elif mod == "Value 1":
        filename = fd.askopenfilename(filetypes=[("All files", "*bin")], title="Select File To Decrypt")
        if filename != "":
            passkey_path = fd.askopenfilename(filetypes=[("Text files", "*.tf")], title="Select Password")
            if passkey_path != "":
                print("Decrypt File")
                decrypter.decrypter_method(filename, passkey_path)
                print(filename)
                subprocess.Popen('explorer "Operations"')


r1 = tk.Radiobutton(form, text='Encrypt File', activebackground="green", value='Value 2',
                    variable=secilen, font=myFont2)
r1.pack()

r2 = tk.Radiobutton(form, text='Decrypt File', activebackground="red", value='Value 1',
                    variable=secilen, font=myFont2)
r2.pack()

c1 = tk.Checkbutton(form, text='Delete Parent File After Encryption', variable=checkbox_secilen,
                    onvalue=1, offvalue=0, padx=5, pady=1, anchor="center")
c1.pack()

b1 = tk.Button(form, text="Confirm", command=confirm, relief="ridge", padx=24, pady=3)
b1.pack()

form.mainloop()
