"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk
from tkinter import *
window=tk.Tk()

frame1=Frame()
label1=Label(frame1,text="enter a adjective: ")
entry1=Entry(frame1)
frame2=Frame()
label2=Label(frame2,text="enter a name: ")
entry2=Entry(frame2)
frame3=Frame()
label3=Label(frame3,text="enter a noun: ")
entry3=Entry(frame3)
frame4=Frame()
label4=Label(frame4,text="enter a plural noun: ")
entry4=Entry(frame4)
frame5=Frame()
label5=Label(frame5,text="enter a adjective: ")
entry5=Entry(frame5)

output1=StringVar()
output2=StringVar()
output3=StringVar()
output4=StringVar()
output5=StringVar()
text1=StringVar()
text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()

def madlibs():
    output1.set(entry1.get())
    output2.set(entry2.get())
    output3.set(entry3.get())
    output4.set(entry4.get())
    output5.set(entry5.get())
    text1.set("There this")
    text2.set("guy named")
    text3.set("who brings")
    text4.set("To all the")
    text5.set("who have been")

button1=Button(window,text="click",command=madlibs)

ff1=Frame()
ffl1=Label(ff1,textvariable=text1)
ffl2=Label(ff1,textvariable=output1)
ff2=Frame()
ffl3=Label(ff2,textvariable=text2)
ffl4=Label(ff2,textvariable=output2)
ff3=Frame()
ffl5=Label(ff3,textvariable=text3)
ffl6=Label(ff3,textvariable=output3)
ff4=Frame()
ffl7=Label(ff4,textvariable=text4)
ffl8=Label(ff4,textvariable=output4)
ff5=Frame()
ffl9=Label(ff5,textvariable=text5)
ffl10=Label(ff5,textvariable=output5)

frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
frame2.pack()
label2.pack(side=LEFT)
entry2.pack(side=LEFT)
frame3.pack()
label3.pack(side=LEFT)
entry3.pack(side=LEFT)
frame4.pack()
label4.pack(side=LEFT)
entry4.pack(side=LEFT)
frame5.pack()
label5.pack(side=LEFT)
entry5.pack(side=LEFT)
button1.pack()
ff1.pack()
ffl1.pack(side=LEFT)
ffl2.pack(side=LEFT)
ff2.pack()
ffl3.pack(side=LEFT)
ffl4.pack(side=LEFT)
ff3.pack()
ffl5.pack(side=LEFT)
ffl6.pack(side=LEFT)
ff4.pack()
ffl7.pack(side=LEFT)
ffl8.pack(side=LEFT)
ff5.pack()
ffl9.pack(side=LEFT)
ffl10.pack(side=LEFT)

window.mainloop()
