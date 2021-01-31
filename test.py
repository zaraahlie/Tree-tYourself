from tkinter import *

window = Tk()
window.geometry('600x400')

window.title("Tree stuff")

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)
window.columnconfigure(5,weight=1)
window.columnconfigure(6,weight=1)

window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)


def clear():
    list = window.grid_slaves()
    for l in list:
        l.destroy()
    print("screen has been cleared")

def confirm_name(name):
    print("confirmation")
    clear()
    lbl = Label(window, text="Is "+name+" your name?",font=("Arial", 20),bg='OliveDrab1')

    lbl.grid(column=3, row=0)

    yes_btn = Button(window, text="yes",font=("Arial", 20), bg='blue', command=instruction_screen)

    yes_btn.grid(column=2, row=2)

    no_btn = Button(window, text="no",font=("Arial", 20), bg='blue', command=name_screen)

    no_btn.grid(column=4, row=2)

def name_screen():
    print("name time")
    clear()

    lbl = Label(window, text="Please enter your name",font=("Arial", 20),bg='OliveDrab1')

    lbl.grid(column=3, row=0)

    txt = Entry(window,width=10,font=("Arial", 20))

    txt.grid(column=3, row=1)

    new_btn = Button(window, text="confirm",font=("Arial", 20), command= lambda: confirm_name(txt.get()))

    new_btn.grid(column=3, row=2)

def start_screen():

    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Tree-t Yourself!", font=("Arial Bold", 40),bg='OliveDrab1')

    lbl.grid(column=3, row=1)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)

    quit_btn.grid(column=4, row=2)

    start_btn = Button(window, text="start",font=("Arial", 20), command=name_screen)

    start_btn.grid(column=2, row=2)

def instruction_screen():
    print("end time")
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="How to Play", font=("Arial Bold", 40),bg='OliveDrab1')
    lbl.grid(column=3, row=0)

    T = Text(window, height=2, width=30)
    T.insert(END, "Find out what tree you are!\nChoose the option that speaks to you\n")
    T.grid(column=3, row=1)

    play_btn = Button(window, text="play",font=("Arial", 20), command=end_screen)

    play_btn.grid(column=3, row=2)

def end_screen():
    print("end time")
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Click to get your tree", font=("Arial Bold", 40),bg='OliveDrab1')

    lbl.grid(column=3, row=1)

    tree_btn = Button(window, text="tree",font=("Arial", 20), command=tree_screen)

    tree_btn.grid(column=4, row=2)


def tree_screen():
    print("end time")
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Your tree is: ", font=("Arial Bold", 40),bg='OliveDrab1')

    lbl.grid(column=3, row=1)
    #get tree

start_screen()

window.mainloop()
