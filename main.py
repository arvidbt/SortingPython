import tkinter
from tkinter import *
from tkinter import ttk
import random
from colors import *

from algorithms.insertion_sort import insertion_sort
from algorithms.bogo_sort import bogo_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort

def generate_UI():
    # GUI
    UI_frame = Frame(window, width=1920, height=1080, bg=BLACK)
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    l1 = Label(UI_frame, text="Sorterings algoritm: ", bg=LIGHT_GRAY)
    l1.grid(row=0, column=0, padx=10, pady=5)
    menu = ttk.Combobox(UI_frame, textvariable=algo_choice, values=algoritms)
    menu.grid(row=0, column=1, padx=5, pady=5)
    menu.current(0)


    l2 = Label(UI_frame, text="Sorterings hastighet: ", bg=LIGHT_GRAY)
    l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    speed = ttk.Combobox(UI_frame, textvariable=algo_speed, values=speeds)
    speed.grid(row=1, column=1, padx=5, pady=5)
    speed.current(0)

    sort_button = Button(UI_frame, text="Sortera: ", command=sort, bg=LIGHT_GREEN)
    sort_button.grid(row=2, column=1, padx=5, pady=5)

    array_button = Button(UI_frame, text="Generera array: ", command=generate, bg=LIGHT_GREEN)
    array_button.grid(row=2, column=0, padx=5, pady=5)

    canvas = Canvas(window, width=1900, height=1080, bg=BLACK)
    canvas.grid(row=1,column=0, padx=10, pady=5)


window = Tk()
window.title("Sorterings algoritmer.")
window.maxsize(2000,1100)
window.config(bg=BLACK)

algoritms = ['bogo_sort', 'bubble_sort', 'insertion_sort', 'quick_sort']
speeds    = ['Långsamt', 'Medium', 'Snabbt', 'SONIIIIC']
algo_choice=StringVar()
algo_speed =StringVar()

data = []
generate_UI()

def drawBars(to_sort, colors_list):
    canvas.delete("all")
    canvas_width = 1920
    canvas_height = 1080
    x_width = canvas_width / (len(to_sort)+1)
    offset  = 5
    spacing = 0.5
    normalized = [i / max(to_sort) for i in data]

    for i, height in enumerate(normalized):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - (height * 800)
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors_list[i])
    
    window.update_idletasks()

def generate():
    global data

    data = []
    for i in range(1, 250):
        random_value = random.randint(1, 250)
        data.append(random_value)
    drawBars(data, [WHITE for x in range(len(data))])

def set_sort_speed():
    if speed.get() == 'Långsamt':
        return 0.5

    elif speed.get() == 'Medium':
        return 0.3

    elif speed.get() == 'Snabbt':
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