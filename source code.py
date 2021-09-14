import easygui  # to open the filebox
import tkinter as tk
from tkinter import *

top = tk.Tk()
top.geometry('500x500')
top.title('Cartoonify Your Image !')
top.configure(background='white')


def upload():
    ImagePath = easygui.fileopenbox()


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5, background='#000000',
                foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
