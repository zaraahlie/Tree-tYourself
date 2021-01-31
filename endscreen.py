from tkinter import *
import test.py

window = Tk()

window.geometry('600x400')

def start_screen():

    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Tree-t Yourself!", font=("Arial Bold", 40),bg='OliveDrab1')

    lbl.grid(column=3, row=1)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)

    quit_btn.grid(column=4, row=2)

    start_btn = Button(window, text="start",font=("Arial", 20), command=name_screen)

    start_btn.grid(column=2, row=2)
