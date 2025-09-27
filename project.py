import tkinter as tk
from tkinter import *

def click(num):
    e.configure(fg="Black")
    e.insert(END , num)

def add():
    e.configure(fg="Black")
    e.insert(90, "+")

def minus():
    e.configure(fg="Black")
    e.insert(90, "-")

def divided():
    e.configure(fg="Black")
    e.insert(90, "/")

def multeplay():
    e.configure(fg="Black")
    e.insert(90, "x")

def dleate():
    e.delete(0, last=90)

def equal():
    amil = e.get()
    if "+" in amil:
        list = amil.split("+")
        result= float(list[0]) + float(list[1])

    elif "-" in amil:
        list = amil.split("-")
        result= float(list[0]) - float(list[1])

    elif "x" in amil:
        list = amil.split("x")
        result= float(list[0]) * float(list[1])

    elif "/" in amil:
        list = amil.split("/")
        if float(list[1]) == 0:
            result= ("cant divided by zero")
        else:
            result= float(list[0]) / float(list[1])

    else:
        result = "ERROR"

    dleate()
    if result in ["ERROR",  "cant divided by zero"]:
        e.configure(fg="red")
    else:
        e.configure(fg='black')

    e.insert(0, result)
 


#حجم الواجهه
face = tk.Tk()
face.title("hamdan calculater")
face.geometry("400x470")

#عشان محد يغر حجم الواججهه
face.resizable(0,0)

#لون الخلفيه
face.configure(bg="black")

#ازرار الواجهه
e = Entry(face, bd=10, width=30, font="arial 26", bg="lightgrey")
e.pack()
e.bind("<Key>", lambda event: e.config(fg="black"))

btn1 = Button(face, text=7 , font="arial 21" , bg="grey", bd=10, padx=15 , pady=15, command=lambda: click(7))
btn1.place(x=10, y =70)

btn2 = Button(face, text=8, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(8) )
btn2.place(x= 95 , y=70)

btn3 = Button(face, text=9, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(9) )
btn3.place(x= 180 , y=70)

btn4 = Button(face, text=4, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(4) )
btn4.place(x= 10 , y=170)

btn5 = Button(face, text=5, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(5) )
btn5.place(x= 95 , y=170)

btn6 = Button(face, text=6, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(6) )
btn6.place(x= 180 , y=170)

btn7 = Button(face, text=1, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(1) )
btn7.place(x= 10 , y=270)

btn8 = Button(face, text=2, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(2))
btn8.place(x= 95 , y=270)

btn9 = Button(face, text=3, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(3) )
btn9.place(x= 180 , y=270)

btn10 = Button(face, text=0, font="arial 21", bd=10 , bg='grey' , padx=15 , pady= 15, command=lambda: click(0) )
btn10.place(x= 95 , y=370)

btn11 = Button(face, text= ".", font= "arial 21", bd=10 , bg="grey", padx=18 , pady=15, command=lambda: click(".") )
btn11.place(x=10, y = 370)

btn12 = Button(face, text= "=", font="arial 21" , bd=10 , bg="lightgreen", padx=81 , pady=15, command= equal)
btn12.place(x=180, y=370)

btn13 = Button(face, text= "c", font="arial 21" , bd=10 , bg="red", padx=40 , pady=15, command= dleate)
btn13.place(x=265, y=270)

btn14 = Button(face, text="+", font="arial 21" , bg="lightblue", bd=10, padx=5 , pady=15, command= add)
btn14.place(x=265, y =70)

btn15 = Button(face, text="-", font="arial 21" , bg="lightblue", bd=10, padx=9 , pady=15, command= minus)
btn15.place(x=330, y =70)

btn16 = Button(face, text="/", font="arial 21" , bg="lightblue", bd=10, padx=9 , pady=15, command= divided)
btn16.place(x=330, y =170)

btn17 = Button(face, text="x", font="arial 21" , bg="lightblue", bd=10, padx=7 , pady=15, command= multeplay)
btn17.place(x=265, y =170)

#لازم عشان تفتح الواجهه
face.mainloop()