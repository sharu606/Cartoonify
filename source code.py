import cv2
import easygui  # to open the filebox
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt

top = tk.Tk()
top.geometry('500x500')
top.title('Cartoonify Your Image !')
top.configure(background='white')


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(imagePath: str):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    resized1 = cv2.resize(image, (1000, 1000))

    plt.imshow(resized1, cmap='gray')
    plt.show()


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5, background='#000000',
                foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
