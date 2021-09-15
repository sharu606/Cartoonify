import cv2
import sys
import os
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
    images = []

    # Step 1 -- Read the image
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    images += cv2.resize(image, (1000, 1000)),

    # confirm that image is chosen
    if image is None:
        print("Cannot find any image. Choose appropriate file")
        sys.exit()

    # Step 2 -- Convert it into gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    images += cv2.resize(gray_image, (1000, 1000)),

    # Step 3 -- Blur the image
    blur_image = cv2.GaussianBlur(gray_image, (9, 9), 0)
    images += cv2.resize(blur_image, (1000, 1000)),

    # Step 4 -- get the edges
    edges = cv2.adaptiveThreshold(blur_image, 255,
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
    images += cv2.resize(edges, (1000, 1000)),

    # Step 5 -- Color mask
    colors = cv2.medianBlur(image, 17)
    images += cv2.resize(colors, (1000, 1000)),

    # Step 6 -- mask edges and colors
    output = cv2.bitwise_and(colors, colors, mask=edges)
    images += cv2.resize(output, (1000, 1000)),

    fig, axes = plt.subplots(3, 2, subplot_kw={'xticks': [], 'yticks': []}, figsize=(8, 8),
                             gridspec_kw={'hspace': 0.1, 'wspace': 0.1})

    for i, axe in enumerate(axes.flatten()):
        axe.imshow(images[i], cmap='gray')

    save1 = Button(top, text="Save cartoon image", command=lambda: save(imagePath, images[-1]), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)

    plt.show()


def save(imagePath: str, image: [[int]]):
    new_name, extension = os.path.splitext(imagePath)
    path = new_name + "_Cartoonified_Image" + extension

    cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    I = "Image saved" + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5, background='#000000',
                foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()
