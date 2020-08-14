from tkinter import *
from functools import partial
import math
cal = Tk()
cal.geometry("600x600")
cal.title("Calculator")
def calcu(op):
    global po,ope,co,i,j,k
    if(po==-1 and isinstance(op,int)):
        ent.insert(i,op)
        i = i+1
    elif(op=="."):
        ent.insert(i, op)
        i = i + 1
    elif (op == "AC"):
        ent.delete(0, END)
        po = -1
        ope = ""
        co = -1
        i = 0
        j = -1
        k = 1
    elif(op=="C"):
         if(po!=-1 and op!=""):
            if(ent.get().find(ope)!= -1):
                ent.delete(i - 1, i)
                i = i - 1
                if(ent.get().find(ope) == -1):
                    ope = ""
                    po=-1
                else:
                    j=j//10
                    k=k-1
         elif(po==-1):
            ent.delete(i - 1, i)
            i = i - 1
    elif (isinstance(op, str) and ent.get() == ""):
        return
    elif (isinstance(op, str) and op!="=" and ope!=""):
        return
    elif(isinstance(op,str) and po==-1):
        if(ent.get().find(".")!=-1):
            po=float(ent.get())
        else:
            po = int(ent.get())
        ope = op
        ent.insert(i, ope)
        i=i+1
    elif(isinstance(op,int) and po!=-1 and ope!=""):
        ent.insert(i, op)
        i = i + 1
        if j==-1:
            j=op
        else:
            j=j*pow(10,k)+op
            k=k+1
    elif(isinstance(op,str) and po!=-1 and ope!=""):
        co=j
        if(op=="="):
            ent.delete(0, END)
            if(ope=="+"):
                ent.insert(0,po+co)
                i=len(str(po+co))+1
                po = -1
                co = -1
            elif(ope == "-"):
                ent.insert(0, po-co)
                i = len(str(po-co))+1
                po = -1
                co = -1
            elif(ope == "x"):
                ent.insert(0, po*co)
                i = len(str(po*co)) + 1
                po = -1
                co = -1
            elif(ope == "/"):
                ent.insert(0, po//co)
                i = len(str(po//co)) + 1
                po = -1
                co = -1
            elif(ope == "%"):
                ent.insert(0, po%co)
                i = len(str(po%co)) + 1
                po = -1
                co = -1
            elif(ope == "^"):
                ent.insert(0, po**co)
                i = len(str(po**co)) + 1
                po = -1
                co = -1
            j = -1
            k = 1
        else:
            ent.delete(0, END)
            if (ope == "+"):
                ent.insert(0, po + co)
                i = len(str(po + co)) + 2
                po = po + co
                co = -1
            elif (ope == "-"):
                ent.insert(0, po - co)
                i = len(str(po - co)) + 2
                po = po - co
                co = -1
            elif (ope == "x"):
                ent.insert(0, po * co)
                i = len(str(po * co)) + 2
                po = po * co
                co = -1
            elif (ope == "/"):
                ent.insert(0, po // co)
                i = len(str(po // co)) + 2
                po = po // co
                co = -1
            elif (ope == "%"):
                ent.insert(0, po % co)
                i = len(str(po % co)) + 2
                po = po % co
                co = -1
            elif (ope == "^"):
                ent.insert(0, po ** co)
                i = len(str(po ** co)) + 2
                po = po % co
                co = -1
            ope = op
            ent.insert(i - 1, ope)
            j = -1
            k = 1
ent = Entry(width=20,font="large_font")
ent.pack()
f1 = Frame(bg="grey",padx=34,pady=71,borderwidth=5,relief=SUNKEN)
f1.pack(anchor=N,side=TOP)
po = -1
ope = ""
co = -1
i=0
j=-1
k=1
but = Button(f1,text="C",padx=3,pady=4,command=partial(calcu,"C"))
but.grid(row=2,column=0)
but = Button(f1,text="AC",padx=2,pady=4,command=partial(calcu,"AC"))
but.grid(row=2,column=1)
but = Button(f1,text="%",padx=4,pady=4,command=partial(calcu,"%"))
but.grid(row=2,column=2)
but = Button(f1,text="/",padx=4,pady=4,command=partial(calcu,"/"))
but.grid(row=2,column=3)
but = Button(f1,text=7,padx=4,pady=4,command=partial(calcu,7))
but.grid(row=3,column=0)
but = Button(f1,text=8,padx=7,pady=4,command=partial(calcu,8))
but.grid(row=3,column=1)
but = Button(f1,text=9,padx=6,pady=4,command=partial(calcu,9))
but.grid(row=3,column=2)
but = Button(f1,text="x",padx=4,pady=4,command=partial(calcu,"x"))
but.grid(row=3,column=3)
but = Button(f1,text=4,padx=4,pady=4,command=partial(calcu,4))
but.grid(row=4,column=0)
but = Button(f1,text=5,padx=7,pady=4,command=partial(calcu,5))
but.grid(row=4,column=1)
but = Button(f1,text=6,padx=6,pady=4,command=partial(calcu,6))
but.grid(row=4,column=2)
but = Button(f1,text="-",padx=4,pady=4,command=partial(calcu,"-"))
but.grid(row=4,column=3)
but = Button(f1,text=1,padx=4,pady=4,command=partial(calcu,1))
but.grid(row=5,column=0)
but = Button(f1,text=2,padx=7,pady=4,command=partial(calcu,2))
but.grid(row=5,column=1)
but = Button(f1,text=3,padx=6,pady=4,command=partial(calcu,3))
but.grid(row=5,column=2)
but = Button(f1,text="+",padx=2,pady=4,command=partial(calcu,"+"))
but.grid(row=5,column=3)
but = Button(f1,text="=",padx=3,pady=4,command=partial(calcu,"="))
but.grid(row=6,column=0)
but = Button(f1,text="^",padx=7,pady=4,command=partial(calcu,"^"))
but.grid(row=6,column=1)
but = Button(f1,text=0,padx=6,pady=4,command=partial(calcu,0))
but.grid(row=6,column=2)
but = Button(f1,text=".",padx=4,pady=4,command=partial(calcu,"."))
but.grid(row=6,column=3)
cal.mainloop()