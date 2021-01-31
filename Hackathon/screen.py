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


def confirm_name(name):

    clear()
    lbl = Label(window, text="Is "+name+" your name?",font=("Arial", 20),bg='OliveDrab1')

    lbl.grid(column=3, row=0)

    yes_btn = Button(window, text="yes",font=("Arial", 20), command=determineScreen)

    yes_btn.grid(column=2, row=2)

    no_btn = Button(window, text="no",font=("Arial", 20), command=name_screen)

    no_btn.grid(column=4, row=2)

def name_screen():

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
    next_screen = ""

    lbl = Label(window, text="Your tree is: " +tree, font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=3, row=1)
    #"Cherry Tree","Money Tree", "Rainbow Tree", "Pando Aspen", "Dragon's Blood Tree", "Kauri Tree"
    if tree=="Cherry Tree":
        next_screen = factsScreen0
    elif tree=="Money Tree":
        next_screen = factsScreen1
    elif tree=="Rainbow Tree":
        next_screen = factsScreen2
    elif tree=="Pando Aspen":
        next_screen = factsScreen3
    elif tree=="Dragon's Blood Tree":
        next_screen = factsScreen4
    elif tree=="Kauri Tree":
        next_screen = factsScreen5

    next_btn = Button(window, text="next",font=("Arial", 20), command=next_screen)
    next_btn.grid(column=4, row=2)



def factsScreen0():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "Known as \"sakura\" in Japanese, these pale blooms are a symbol of spring because it is a time of renewal. However, because the blooms are short-lived, they are also symbolic of the fleeting nature of life.\n")
    T1.grid(column=1, row=1)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "The ornamental Japanese cherry trees we are used to seeing average 20 to 40 feet with canopies that can reach between 15 and 30 feet. Wild cherry trees can grow up to 80 feet tall.\n")
    T2.grid(column=1, row=2)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, "Flowers can range in color from pale pink to bright pink as well as white and ivory. For example, in Washington D.C. 70% of the trees are made up of Yoshinos which have single white blossoms. However, because they are mixed in with Akebono cherry trees, the Yoshino has mutated to present pale pink blossoms.\n")
    T3.grid(column=1, row=3)

    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Source: https://www.countryliving.com/gardening/g3168/cherry-blossoms-facts/\n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)

def factsScreen1():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "Rumored to bring luck and prosperity to the owner, there’s good reason money trees are popular gifts for executives and frequently used as office décor.\n")
    T1.grid(column=1, row=1)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "Most money trees have five or six leaves on each stem, but you’ll occasionally find one with seven leaves on each stem. If you do, you might want to consider buying a lottery ticket—seven leaf stems are rumored to bring extra luck.\n")
    T2.grid(column=1, row=2)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, "The wild Money Plants generally grows up to 50-60 feet tall – thus they can be called a Monet Tree. But when you grow it in a pot in your home, it would reach 10-15 feet only. So, the environment makes all the difference!\n")
    T3.grid(column=1, row=3)

    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Source: https://www.easternleaf.com/What_Is_A_Money_Tree_Plant_a/445.htm\nhttps://www.fnp.com/blog/12-amazing-facts-about-money-plants\n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)

def factsScreen2():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "Rainbow eucalyptus (Eucalyptus deglupta) is the only eucalyptus tree indigenous to the northern hemisphere. It grows in the Philippines, New Guinea, and Indonesia where it thrives in tropical forests that get a lot of rain. The tree grows up to 250 feet (76 m.) tall in its native environment.\n")
    T1.grid(column=1, row=1)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "Aside from climate, rainbow eucalyptus growing conditions include full sun and moist soil. Once established, the tree grows 3 feet per season without supplemental fertilizer, although it needs regular watering when rainfall is insufficient.\n")
    T2.grid(column=1, row=2)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, "The most outstanding feature of a rainbow eucalyptus tree is its bark. The previous season’s bark peels off in strips to reveal a brightly colored new bark below. The peeling process results in vertical streaks of red, orange, green, blue and gray. Although the tree’s color isn’t as intense outside its native range, rainbow eucalyptus bark color makes it one of the most amazingly colorful trees you can grow.\n")
    T3.grid(column=1, row=3)

    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Source: https://www.gardeningknowhow.com/ornamental/trees/eucalyptus/rainbow-eucalyptus-tree.htm\n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)


def factsScreen3():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "The Trembling Giant, or Pando, is an enormous grove of quaking aspens that take the “forest as a single organism” metaphor and makes it literal: the grove really is a single organism. Each of the approximately 47,000 or so trees in the grove is genetically identical and all the trees share a single root system. \n")
    T1.grid(column=1, row=1)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "Quaking aspens usually reproduce asexually, by sprouting new trees from the expansive lateral root of the parent. The individual trees aren’t individuals but stems of a massive single clone\n")
    T2.grid(column=1, row=2)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, " it one of the world’s oldest living organisms. Some of the trees in the forest are over 130 years old.\n")
    T3.grid(column=1, row=3)

    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Source: https://www.atlasobscura.com/places/pando-the-trembling-giant#:~:text=The%20Trembling%20Giant%2C%20or%20Pando,share%20a%20single%20root%20system. \n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)


def factsScreen4():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "The dragon blood tree is an unique tree native to the Socotra archipelago, part of Yemen, located in the Arabian Sea. \n")
    T1.grid(column=1, row=1)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "The dragon blood tree is an evergreen tree that can live up to 650 years and reaches heights of around 10 to 12 meters (33 to 39 feet). It branches at maturity to produce an umbrella-shaped crown, with leaves that measure up to 60 cm (23.6 in) long and 3 cm (1.2 in) wide.\n")
    T2.grid(column=1, row=2)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, "Because of the belief that it is the blood of the dragon it is also used in ritual magic and alchemy.\n")
    T3.grid(column=1, row=3)

    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Source: http://justfunfacts.com/interesting-facts-about-dragon-blood-trees/#:~:text=The%20dragon%20blood%20tree%20is%20an%20evergreen%20tree%20that%20can,very%20hardy%20and%20drought%20tolerant.\n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)


def factsScreen5():
    clear()
    window.configure(bg='OliveDrab1')

    lbl = Label(window, text="Facts", font=("Arial Bold", 20),bg='OliveDrab1')
    lbl.grid(column=1, row=0)

    T1 = Text(window, height=5, width=50)
    T1.insert(END, "Agathis australis, commonly known by its Māori name kauri, is a coniferous tree of Araucariaceae in the genus Agathis, found north of 38°S in the northern districts of New Zealand's North Island\n")
    T1.grid(column=1, row=3)

    T2 = Text(window, height=5, width=50)
    T2.insert(END, "On average Kauri trees are large, about 30-40 meters tall with a trunk diameter of several meters. That is big, but a few of them grow into an immense size. These trees are the second largest tree in the world by trunk volume.\n")
    T2.grid(column=1, row=1)

    T3 = Text(window, height=5, width=50)
    T3.insert(END, "Kauri trees can live for a very, very long time. scientists estimate that Tane Mahuta is 2,000 years old. Te Matua Ngahere is suspected to be even older, up to 2,500 years old! Just to put that in perspective, the modern calendar started 2,000 years ago!\n")
    T3.grid(column=1, row=2)



    T4 = Text(window, height=3, width=50)
    T4.insert(END, "Sources: https://en.wikipedia.org/wiki/Agathis_australis\n https://www.nznatureguy.com/2019/08/28/7-kauri-facts-newzealand-giant-tree/ \n")
    T4.grid(column=1, row=4)

    quit_btn = Button(window, text="quit",font=("Arial", 20), command=exit)
    quit_btn.grid(column=4, row=2)
