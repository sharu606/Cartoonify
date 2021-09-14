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

    # Step 1 -- Read the image
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    resized1 = cv2.resize(image, (1000, 1000))

    # Step 2 -- Convert it into gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    resized2 = cv2.resize(gray_image, (1000, 1000))

    # Step 3 -- Blur the image
    blur_image = cv2.GaussianBlur(gray_image, (9, 9), 0)
    resized3 = cv2.resize(blur_image, (1000, 1000))

    # Step 4 -- get the edges
    edges = cv2.adaptiveThreshold(blur_image, 255,
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
    resized4 = cv2.resize(edges, (1000, 1000))

    # Step 5 -- Color mask
    colors = cv2.medianBlur(image, 17)
    resized5 = cv2.resize(colors, (1000, 1000))

    # Step 6 -- mask edges and colors
    output = cv2.bitwise_and(colors, colors, mask=edges)
    resized6 = cv2.resize(output, (1000, 1000))

    plt.imshow(resized6, cmap='gray')
    plt.show()


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5, background='#000000',
                foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
