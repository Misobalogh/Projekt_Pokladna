def main():
    pass


from tkinter import *


def dokoncenie_platby():
    global polozky

    for potraviny in listbox.curselection():
        polozky.insert(potraviny, listbox.get(potraviny))

    for potraviny in polozky:
        print(potraviny)


def enter():
    global polozky
    listbox.insert(listbox.size(), entry.get())
    potravina = entry.get()
    polozky.append(potravina)
    entry.delete(0, END)
    listbox.config(height=listbox.size())


def storno_riadku():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())


def storno():
    listbox.delete(0, END)
    listbox.config(height=listbox.size())




def pecivo():
    global pec, canvas
    canvas = Canvas(window, width=500, height=500)
    canvas.place(x=1 / 6 * w, y=2 / 12 * h + 1 / 18 * h)
    canvas.create_rectangle(0, 0, 1 / 6 * w + 200, 2 / 6 * h + 100, fill='#E0DA63')
    pec = Listbox(canvas, width=16, bg="#98C352", font=("Roboto", 35))
    pec.insert(1, "biely rozok")
    pec.insert(2, "grahamovy rozok")
    pec.insert(3, "zemla")
    pec.insert(4, "kaiserka")
    check = Button(canvas, text="Potvrdiť", width=int(w / 150), font="Roboto 20", bg="#98C352", fg="white",
                   activebackground="#E0DA63", activeforeground="black",
                   borderwidth=0, cursor="hand2",
                   command = moreuzmamnervy)
    check.place(x=1 / 12 * w, y=2 / 6 * h)

    pec.pack()

def ovozel():
    global ovozel, canvas
    canvas = Canvas(window, width=500, height=500)
    canvas.place(x=1 / 6 * w, y=2 / 12 * h + 1 / 18 * h)
    canvas.create_rectangle(0, 0, 1 / 6 * w + 200, 2 / 6 * h + 100, fill='#E0DA63')
    ovozel = Listbox(canvas, width=16, bg="#98C352", font=("Roboto", 35))
    ovozel.insert(1, "hruska")
    ovozel.insert(2, "jabko")
    ovozel.insert(3, "zemla")
    ovozel.insert(4, "kaiserka")
    check = Button(canvas, text="Potvrdiť", width=int(w / 150), font="Bahnschrift 20", bg="#98C352", fg="white",
                   activebackground="#E0DA63", activeforeground="black",
                   borderwidth=0, cursor="hand2",
                   command = moreuzmamnervy2)
    check.place(x=1 / 12 * w, y=2 / 6 * h)

    ovozel.pack()

def moreuzmamnervy():
    listbox.insert(listbox.size(), pec.get(pec.curselection()))
    canvas.destroy()

def moreuzmamnervy2():
    listbox.insert(listbox.size(), ovozel.get(ovozel.curselection()))
    canvas.destroy()


def create_buttons():
    # storno_img = PhotoImage(file="storno.png")
    platbaButton = Button(window, text="Dokončiť platbu", width=int(w / 90), font="Bahnschrift 20", bg="#98C352",
                          fg="white", activebackground="#E0DA63", activeforeground="black",
                          cursor="hand2", command=dokoncenie_platby)
    platbaButton.place(x=4 / 6 * w, y=2 / 12 * h)

    enterButton = Button(window, text="Enter", width=int(w / 90), font="Bahnschrift 20", bg="#98C352", fg="white",
                         activebackground="#E0DA63", activeforeground="black",
                         cursor="hand2", command=enter)
    enterButton.place(x=4 / 6 * w, y=3 / 12 * h)

    deleteButton = Button(window, text="Storno riadku", width=int(w / 90), font="Bahnschrift 20", bg="#98C352",
                          fg="white", activebackground="#E0DA63", activeforeground="black",
                          cursor="hand2", command=storno_riadku)
    deleteButton.place(x=4 / 6 * w, y=4 / 12 * h)

    stornoButton = Button(window, text="Storno", width=int(w / 90), font="Bahnschrift 20", bg="#98C352", fg="white",
                          activebackground="#E0DA63", activeforeground="black",
                          cursor="hand2", command=storno)
    stornoButton.place(x=4 / 6 * w, y=5 / 12 * h)

    pecivoButton = Button(window, text="Pečivo", width=int(w / 90), font="Bahnschrift 20", bg="#98C352",
                          fg="white", activebackground="#E0DA63", activeforeground="black",
                          cursor="hand2", command=pecivo)
    pecivoButton.place(x= 1 / 6 * w, y=2 / 12 * h)

    ovozelButton = Button(window, text="Ovocie a Zelenina", width=int(w / 90), font="Bahnschrift 20", bg="#98C352",
                          fg="white", activebackground="#E0DA63", activeforeground="black",
                          cursor="hand2", command=ovozel)
    ovozelButton.place(x= 2 / 6 * w, y=2 / 12 * h)


window = Tk()

polozky = []

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(h, w)

window.attributes("-fullscreen", True)
window.bind("<F11>", lambda event: window.attributes("-fullscreen",
                                                     not window.attributes("-fullscreen")))
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False), window.geometry('1000x600'))

listbox = Listbox(window,
                  bg="#faf7ca",
                  font=("Roboto", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

# frame = Frame(window)
# frame.pack()
create_buttons()

pecivo = Menu(window)
window.config(menu=pecivo)

klasicke_pecivo = Menu(pecivo)
pecivo.add_cascade(label="Pecivo", menu=klasicke_pecivo)
klasicke_pecivo.add_command(label="Biely rozok", command=lambda: None)
klasicke_pecivo.add_command(label="Grahamovy rozok", command=lambda: None)

window.mainloop()

if __name__ == '__main__':
    main()
