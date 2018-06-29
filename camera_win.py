# -*- coding: utf-8 -*-
import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk

global _video, uri, uri_entry
_video = 'Disabled'

#Настройка интерфейса
window = tk.Tk()  #Создание главного окна
window.wm_title("НашАКо")
window.config(background="#FFFFFF")

#Видео
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Захват видео
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
global cap
def show_frame():
        global _video, cap, uri
        if _video == 'Enabled':
                _, frame = cap.read()
                if _:
                        cv2image = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
                        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
                        img = Image.fromarray(cv2image)
                        imgtk = ImageTk.PhotoImage(image=img)
                        lmain.imgtk = imgtk
                        lmain.configure(image=imgtk)
                else:
                        print 'Wait...'
                        cap = cv2.VideoCapture(uri.get())
                lmain.after(10, show_frame)

def start(event):
        global _video, cap, uri
        if _video == 'Enabled':
                _video = 'Disabled'
                return
        elif _video == 'Disabled' and uri.get():
                _video = 'Enabled'
                cap = cv2.VideoCapture(uri.get())
                show_frame()
                return;
#Кнопка старта
btn = tk.Button(window, text = 'Start', width = 30, height = 5)
btn.grid(row = 3, column = 0, padx = 2, pady = 2)
btn.bind("<Button-1>", start)

#Строка ввода адреса
uri = tk.StringVar()
uri_entry = tk.Entry(textvariable = uri)
uri_entry.grid(row = 2, column = 0, padx = 2, pady = 2)

#Размеры окна
#sliderFrame = tk.Frame(window, width=600, height=100)
#sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

show_frame()  #Запуск видеозахвата
window.mainloop()  #Запуск интерфейса
