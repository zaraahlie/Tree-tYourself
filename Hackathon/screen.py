from tkinter import *
from game import *

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

    yes_btn = Button(window, text="yes",font=("Arial", 20), command=determineScreen)

    yes_btn.grid(column=2, row=2)

    no_btn = Button(window, text="no",font=("Arial", 20), command=name_screen)

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


def path_screen2(ques1, ques2):
    clear()
    #creates the window
    window.configure(bg='OliveDrab1')

    #collects the correct question
    

    lbl = Label(window, text= ques1 + " or " + ques2 ,font=("Arial", 20),bg='OliveDrab1')
    lbl.grid(column=3, row=0)

    question1 = Button(window, text=ques1,font=("Arial", 20), command=addDirectionL)

    question1.grid(column=2, row=2)

    question2 = Button(window, text=ques2,font=("Arial", 20), command=addDirectionR)

    question2.grid(column=4, row=2)

def path_screen3(ques1, ques2, ques3):
    clear()
    #creates the window
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text= ques1 + " or " + ques2 ,font=("Arial", 20),bg='OliveDrab1')
    lbl.grid(column=3, row=0)

    question1 = Button(window, text=ques1,font=("Arial", 20), command=addDirectionL)

    question1.grid(column=2, row=2)

    question2 = Button(window, text=ques2,font=("Arial", 20), command=addDirectionM)

    question2.grid(column=3, row=2)

    question3 = Button(window, text=ques3,font=("Arial", 20), command=addDirectionR)

    question3.grid(column=4, row=2)

def endScreen(tree):
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Your tree is: " +tree, font=("Arial Bold", 20),bg='OliveDrab1')

    lbl.grid(column=3, row=1)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)