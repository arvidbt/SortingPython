import tkinter
from tkinter import *
from tkinter import ttk
import random
from colors import *

from algorithms.insertion_sort import insertion_sort
from algorithms.bogo_sort import bogo_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort


window = Tk()
window.title("Sorting Algorithms")
window.maxsize(1000,700)
window.config(bg=WHITE)

algoritms = ['bogo_sort', 'bubble_sort', 'insertion_sort', 'quick_sort']
speeds    = ['fast', 'medium', 'slow', 'SONIIIIC']
algo_choice=StringVar()
algo_speed =StringVar()

data = []

def drawBars(to_sort, colors_list):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400

    x_width = canvas_width / (len(to_sort) + 1)
    offset  = 4
    spacing = 2
    normalized = [i  / max(to_sort) for i in data]

    for i, height in enumerate(normalized):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors_list[i])
    
    window.update_idletasks()

def generate():
    global data

    data = []
    for i in range(1, 150):
        random_value = random.randint(1, 150)
        data.append(random_value)
    drawBars(data, [BLUE for x in range(len(data))])

def set_sort_speed():
    if speed.get() == 'slow':
        return 0.5

    elif speed.get() == 'medium':
        return 0.3

    elif speed.get() == 'fast':
        return 0.01

    elif speed.get() == 'SONIIIIC':
        return 0.00001

def sort():
    global data

    timer = set_sort_speed()

    if menu.get()   == 'bogo_sort':
        bogo_sort(data, drawBars, timer)

    elif menu.get() == 'bubble_sort':
        bubble_sort(data, drawBars, timer)

    elif menu.get() == 'insertion_sort':
        insertion_sort(data, drawBars, timer)

    elif menu.get() == 'quick_sort':
        quick_sort(data, 0, len(data)-1, drawBars, timer)

# GUI
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5)
menu = ttk.Combobox(UI_frame, textvariable=algo_choice, values=algoritms)
menu.grid(row=0, column=1, padx=5, pady=5)
menu.current(0)


l2 = Label(UI_frame, text="Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed = ttk.Combobox(UI_frame, textvariable=algo_speed, values=speeds)
speed.grid(row=1, column=1, padx=5, pady=5)
speed.current(0)

sort_button = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
sort_button.grid(row=2, column=1, padx=5, pady=5)

array_button = Button(UI_frame, text="Generate array: ", command=generate, bg=LIGHT_GRAY)
array_button.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1,column=0, padx=10, pady=5)

window.mainloop()