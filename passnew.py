from tkinter import *
import random,string

root=Tk()
root.geometry("380x290")
root.title("password generator")
root.config(bg="light grey")
title=StringVar()
label=Label(root,text="Password Generator",font=('arial',20,'bold'),bg="light grey",fg="grey").pack()
#title.set("password strength")
label=Label(root,text="password strength:",font=('arial',10,'bold'),bg="light grey",fg="grey").pack()
def select():
    select=choice.get()

choice=IntVar()
c1=Radiobutton(root,text="POOR",font=('arial',10,'bold'),bg="light grey",fg="grey",variable=choice,value=1,command=select).pack(anchor=CENTER)
c2=Radiobutton(root,text="AVERAGE",font=('arial',10,'bold'),bg="light grey",fg="grey",variable=choice,value=2,command=select).pack(anchor=CENTER)
c3=Radiobutton(root,text="STRONG",font=('arial',10,'bold'),bg="light grey",fg="grey",variable=choice,value=3,command=select).pack(anchor=CENTER)
#lablechoice=Label(root).pack()
lenlabel=Label(root,text="password length:",font=('arial',10,'bold'),bg="light grey",fg="grey").pack()
#lenlabel.set("password length:")
#lentitle=Label(root,textvariable=lenlabel).pack()
val=IntVar()
length=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()

def callback():
    lsum.config(text=passgen())
Button(root,text="GENERATE",bd=3,height=2,pady=3,command=callback,bg="light grey").pack()

password=str(callback)
lsum=Label(root,text="",bg="light grey")
lsum.pack(side=BOTTOM)


    #LOGIC
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="!@#$%^&*()?><\_-"
strong=poor+average+symbols

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    if choice.get()==2:
        return"".join(random.sample(average,val.get()))
    
    if choice.get()==3:
        return"".join(random.sample(strong,val.get()))
    
    


