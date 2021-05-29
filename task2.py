"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
from tkinter import *
window=tk.Tk()
import math

def calc():
    b=float(entry1.get())
    c=float(entry2.get())
    delta=float((b**2)-(4*c))
    root=[]

    if delta>=0:
        delta=math.sqrt(float((b**2)-(4*c)))
        r1=(-b+delta)/2
        r2=(-b-delta)/2
        root.append(r1)
        root.append(r2)
    else:
        root.append("no root")
    answer.delete(0,END)
    answer.insert(0,root)

label1=tk.Label(window,text="x^2 +")
entry1=tk.Entry(window,width=5)
label2=tk.Label(window,text="x +")
entry2=tk.Entry(window,width=5)
b1=Button(window,text="=",command=calc)
answer=Entry(window,width=10)

label1.grid(row=1,column=2)
entry1.grid(row=1,column=3)
label2.grid(row=1,column=4)
entry2.grid(row=1,column=5)
b1.grid(row=1,column=6)
answer.grid(row=1,column=7)

window.mainloop()
