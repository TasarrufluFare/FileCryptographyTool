import tkinter as tk
from tkinter import filedialog as fd
from tkinter import font
import encrypter
import decrypter


form = tk.Tk(screenName="File Encrypter")
form.title("File Cryptography")
form.geometry("308x100")
form.minsize(308, 100)
form.maxsize(308, 100)
form.iconphoto(False, tk.PhotoImage(file='icon.png'))
form.configure(background="#301024")
myFont1 = font.Font(family='Courier', size=14, weight='bold')
myFont2 = font.Font(family='Courier', size=10, weight='bold')

secilen = tk.StringVar()


def confirm():
    mod = secilen.get()

    if mod == "Value 2":
        filename = fd.askopenfilename(filetypes=[("All files", "*")])
        print("Encrypt File")
        encrypter.encrypter_method(filename)
        print(filename)

    elif mod == "Value 1":
        filename = fd.askopenfilename(filetypes=[("All files", "*")], title="Select File To Decrypt")
        passkey_path = fd.askopenfilename(filetypes=[("Text files", "*.txt")], title="Select Password")
        if filename != "" and passkey_path != "":
            print("Decrypt File")
            decrypter.decrypter_method(filename, passkey_path)
            print(filename)


r1 = tk.Radiobutton(form, text='Encrypt File', activebackground="green", value='Value 2',
                    variable=secilen, font=myFont2)
r1.pack()
r2 = tk.Radiobutton(form, text='Decrypt File', activebackground="red", value='Value 1',
                    variable=secilen, font=myFont2)
r2.pack()

b1 = tk.Button(form, text="Confirm", command=confirm, relief="ridge", padx=24, pady=3)
b1.pack()

form.mainloop()
