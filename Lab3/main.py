#!/usr/bin/env python3

from tkinter import filedialog as fd

from PIL import Image, ImageTk
from PIL.ImageFilter import CONTOUR


def change_img(new_image):
    global img_label

    print('change_img ', new_image)

    img = Image.open(new_image)
    img = img.convert('RGB')
    img.thumbnail([512, 256])
    img2 = ImageTk.PhotoImage(img)
    img_label.configure(image=img2)
    img_label.image = img2


def save_image_with_another_extension(image_name: str, new_extension: str) -> str:
    """ Функція для збереження зображення з новим типом """

    im = Image.open(image_name)
    image_name_without_extension = ''.join(''.join(image_name.split('.')[:-1]).split('/')[-1])
    im.save(f'{image_name_without_extension}.{new_extension}')

    global current_file, img_name
    current_file = f'{image_name_without_extension}.{new_extension}'
    img_name.config(text=f'Відкритий файл: {current_file}')
    change_img(current_file)
    print(current_file)

    return f'{image_name_without_extension}.{new_extension}'


def change_resolution(x: int, y: int, current_file) -> Image:
    """ Функція для зміни розширення """

    image = Image.open(current_file)
    image = image.resize((x, y), Image.ANTIALIAS)
    image.save(current_file, optimize=True, quality=95)
    change_img(current_file)
    return image


def apply_contour_filter(image_name: str) -> None:
    """ Функція для застосування фільтру """
    image = Image.open(image_name)
    image = image.convert('RGB')
    image = image.filter(CONTOUR)
    image.save(image_name)
    change_img(current_file)

    return image

import tkinter as tk


def choose_file():
    """ Функція для вибору файла """
    global current_file

    filename = fd.askopenfilename()
    filename = filename.split('/')[-1]
    img_name.config(text=f'Відкритий файл: {filename}')

    current_file = filename

    change_img(current_file)

    return filename


if __name__ == "__main__":
    app = tk.Tk()

    new_file_extension = tk.StringVar()
    current_file = tk.StringVar()
    x = tk.StringVar()
    y = tk.StringVar()

    button = tk.Button(app, command=lambda: choose_file(), text='Вибрати файл')
    button.grid(row=0, column=0, columnspan=4)

    img_name = tk.Label(app, text='Відкритий файл: None')
    img_name.grid(row=1, column=0, columnspan=4)

    extension_entry = tk.Entry(textvariable=new_file_extension)
    extension_entry.grid(row=2, column=1)

    img_ext = tk.Label(app, text='Новий тип')
    img_ext.grid(row=2, column=0)
    button_ext = tk.Button(app, command=lambda: save_image_with_another_extension(current_file, new_file_extension.get()),
                       text='Змінити тип файлу')
    button_ext.grid(row=3, column=0)

    img_x = tk.Label(app, text='Ширина')
    img_x.grid(row=4, column=0)
    extension_entry = tk.Entry(textvariable=x)
    extension_entry.grid(row=4, column=1)

    img_y = tk.Label(app, text='Висота')
    img_y.grid(row=5, column=0)
    extension_entry = tk.Entry(textvariable=y)
    extension_entry.grid(row=5, column=1)
    button_res = tk.Button(app, command=lambda: change_resolution(int(x.get()), int(y.get()), current_file),
                       text='Змінити розширення')
    button_res.grid(row=6, column=0)

    button_filter = tk.Button(app, command=lambda: apply_contour_filter(current_file),
                           text='Застосувати фільтр')
    button_filter.grid(row=7, column=0)

    img_label = tk.Label(app)
    img_label.grid(row=8, column=0, columnspan=4)

    app.bind("<Return>", change_img)
    app.title("Image")
    app.geometry("800x600")
    app.mainloop()

    app.mainloop()
