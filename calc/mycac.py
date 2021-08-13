from tkinter import  *
def click(event):
    global  scvalue
    text=event.widget.cget("text")
     #cget function button mathi anu text lave
    print(text)

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="error"



        scvalue.set(value)
        screen.update()


    elif text=="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()






root=Tk()

root.geometry("644x900")
root.title("calculatro by akshar")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

#have ek frame banavishu ne aama button pack karishu

f=Frame(root,bg="grey")

for i in range(7,10):
    b = Button(f, text=f"{i}", font="lucida 30 bold", padx=10, pady=10)
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)

f.pack()
#---------------------------------------------
f=Frame(root,bg="grey")

for i in range(4,7):
    b = Button(f, text=f"{i}", font="lucida 30 bold", padx=10, pady=10)
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)
f.pack()
#---------------------------------------------
f=Frame(root,bg="grey")

for i in range(1,4):
    b = Button(f, text=f"{i}", font="lucida 30 bold", padx=10, pady=10)
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)

f.pack()

#-------------------------------------------

f=Frame(root,bg="grey")
b=Button(f,text="0",font="lucida 32 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 32 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 32 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

#----------------
f=Frame(root,bg="grey")
b=Button(f,text="/",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 30 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="00",font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="c",font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 26 bold",padx=10,pady=10)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()