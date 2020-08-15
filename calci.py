from tkinter import *
from functools import partial
cal = Tk()
cal.geometry("600x600")
cal.title("Calculator")
def calcu(op):
   global i,ope
   if(isinstance(op,int)):
       ent.insert(i,op)
       i=i+1
   elif(op=="."):

       if(ent.get().find("+") == -1 and ent.get().find("-") == -1 and
               ent.get().find("*") == -1 and ent.get().find("/") == -1 and
               ent.get().find("%") == -1 and ent.get().find("^") == -1 and ent.get().find(".") == -1):
           ent.insert(i, op)
           i = i + 1
       elif(ent.get().find("+") == -1 and ent.get().find("-") == -1 and
               ent.get().find("*") == -1 and ent.get().find("/") == -1 and
               ent.get().find("%") == -1 and ent.get().find("^") == -1 and ent.get().find(".") != -1):
           return
       elif (ent.get().find("+") != -1 or ent.get().find("-") != -1 or
             ent.get().find("*") != -1 or ent.get().find("/") != -1 or
             ent.get().find("%") != -1 or ent.get().find("^") != -1):
           if (ent.get()[len(ent.get()) - 1] == "+" or ent.get()[len(ent.get()) - 1] == "-" or
                   ent.get()[len(ent.get()) - 1] == "*" or ent.get()[len(ent.get()) - 1] == "/" or
                   ent.get()[len(ent.get()) - 1] == "%" or ent.get()[len(ent.get()) - 1] == "^"):
               return
           else:
               for j in range(ent.get().find(ope),len(ent.get())):
                   if(ent.get()[j] == "."):
                       return
               ent.insert(i, op)
               i = i + 1
   elif(op=="+" or op=="-" or op=="*" or op=="/" or op=="%" or op=="^"):
       if(ent.get()=="" or ent.get()[len(ent.get())-1]=="+" or ent.get()[len(ent.get())-1]=="-" or
          ent.get()[len(ent.get())-1]=="*" or ent.get()[len(ent.get())-1]=="/" or
          ent.get()[len(ent.get())-1]=="%"or ent.get()[len(ent.get())-1]=="^" or ent.get()[len(ent.get())-1]=="."):
           return
       elif(ent.get().find("+")!=-1 or ent.get().find("-")!=-1 or
            ent.get().find("*")!=-1 or ent.get().find("/")!=-1 or
            ent.get().find("%")!=-1 or ent.get().find("^")!=-1):
           if(ent.get().find("+")!=-1):
               ope = "+"
               a = ent.get().split("+")
               ent.delete(0, END)
               if(a[0].find(".")==-1 and a[1].find(".")==-1):
                   ent.insert(i, int(a[0]) + int(a[1]))
                   i = len(str(int(a[0]) + int(a[1]))) + 1
                   ent.insert(i, op)
                   i=i+1
               elif(a[0].find(".")!=-1 and a[1].find(".")==-1):
                   ent.insert(i, float(a[0]) + int(a[1]))
                   i = len(str(float(a[0]) + int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i+1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) + float(a[1]))
                   i = len(str(int(a[0]) + float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i+1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) + float(a[1]))
                   i = len(str(float(a[0]) + float(a[1]))) + 1
                   ent.insert(i, op)
                   i=i+1
           elif(ent.get().find("-") != -1):
               ope = "-"
               a = ent.get().split("-")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) - int(a[1]))
                   i = len(str(int(a[0]) - int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) - int(a[1]))
                   i = len(str(float(a[0]) - int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) - float(a[1]))
                   i = len(str(int(a[0]) - float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) - float(a[1]))
                   i = len(str(float(a[0]) - float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
           elif(ent.get().find("*") != -1):
               ope = "*"
               a = ent.get().split("*")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) * int(a[1]))
                   i = len(str(int(a[0]) * int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) * int(a[1]))
                   i = len(str(float(a[0]) * int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) * float(a[1]))
                   i = len(str(int(a[0]) * float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) * float(a[1]))
                   i = len(str(float(a[0]) * float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
           elif(ent.get().find("/") != -1):
               ope = "/"
               a = ent.get().split("/")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) / int(a[1]))
                   i = len(str(int(a[0]) / int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) / int(a[1]))
                   i = len(str(float(a[0]) / int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) / float(a[1]))
                   i = len(str(int(a[0]) / float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) / float(a[1]))
                   i = len(str(float(a[0]) / float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
           elif(ent.get().find("%") != -1):
               ope = "%"
               a = ent.get().split("%")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) % int(a[1]))
                   i = len(str(int(a[0]) % int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) % int(a[1]))
                   i = len(str(float(a[0]) % int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) % float(a[1]))
                   i = len(str(int(a[0]) % float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) % float(a[1]))
                   i = len(str(float(a[0]) % float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
           elif(ent.get().find("^") != -1):
               ope = "^"
               a = ent.get().split("^")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) ** int(a[1]))
                   i = len(str(int(a[0]) ** int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) ** int(a[1]))
                   i = len(str(float(a[0]) ** int(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) ** float(a[1]))
                   i = len(str(int(a[0]) ** float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) ** float(a[1]))
                   i = len(str(float(a[0]) ** float(a[1]))) + 1
                   ent.insert(i, op)
                   i = i + 1
       else:
           ent.insert(i, op)
           i=i+1
           ope=op
   if(op=="="):
       if(ent.get().find("+")==-1 and ent.get().find("-")==-1 and
          ent.get().find("*")==-1 and ent.get().find("/")==-1 and
          ent.get().find("%")==-1 and ent.get().find("^")==-1):
           return
       elif(ent.get() == "" or ent.get()[len(ent.get()) - 1] == "+" or ent.get()[len(ent.get()) - 1] == "-" or
               ent.get()[len(ent.get()) - 1] == "*" or ent.get()[len(ent.get()) - 1] == "/" or
               ent.get()[len(ent.get()) - 1] == "%" or ent.get()[len(ent.get()) - 1] == "^"):
           return
       else:
           if(ent.get().find("+")!=-1):
               ope = "+"
               a=ent.get().split("+")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) + int(a[1]))
                   i=len(str(int(a[0]) + int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) + int(a[1]))
                   i=len(str(float(a[0]) + int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) + float(a[1]))
                   i=len(str(int(a[0]) + float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) + float(a[1]))
                   i=len(str(float(a[0]) + float(a[1]))) + 1

           elif(ent.get().find("-")!=-1):
               ope = "-"
               a=ent.get().split("-")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) - int(a[1]))
                   i = len(str(int(a[0]) - int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) - int(a[1]))
                   i = len(str(float(a[0]) - int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) - float(a[1]))
                   i = len(str(int(a[0]) - float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) - float(a[1]))
                   i = len(str(float(a[0]) - float(a[1]))) + 1
           elif(ent.get().find("*")!=-1):
               ope = "*"
               a=ent.get().split("*")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) * int(a[1]))
                   i = len(str(int(a[0]) * int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) * int(a[1]))
                   i = len(str(float(a[0]) * int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) * float(a[1]))
                   i = len(str(int(a[0]) * float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) * float(a[1]))
                   i = len(str(float(a[0]) * float(a[1]))) + 1
           elif(ent.get().find("/")!=-1):
               ope = "/"
               a=ent.get().split("/")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) / int(a[1]))
                   i = len(str(int(a[0]) / int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) / int(a[1]))
                   i = len(str(float(a[0]) / int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) / float(a[1]))
                   i = len(str(int(a[0]) / float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) + float(a[1]))
                   i = len(str(float(a[0])/float(a[1]))) + 1
           elif(ent.get().find("%")!=-1):
               ope = "%"
               a=ent.get().split("%")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0])%int(a[1]))
                   i = len(str(int(a[0]) % int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) % int(a[1]))
                   i = len(str(float(a[0]) % int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) % float(a[1]))
                   i = len(str(int(a[0]) % float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) % float(a[1]))
                   i = len(str(float(a[0]) % float(a[1]))) + 1
           elif(ent.get().find("^")!=-1):
               ope = "^"
               a=ent.get().split("^")
               ent.delete(0, END)
               if (a[0].find(".") == -1 and a[1].find(".") == -1):
                   ent.insert(i, int(a[0]) ** int(a[1]))
                   i = len(str(int(a[0]) ** int(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") == -1):
                   ent.insert(i, float(a[0]) ** int(a[1]))
                   i = len(str(float(a[0]) ** int(a[1]))) + 1
               elif (a[0].find(".") == -1 and a[1].find(".") != -1):
                   ent.insert(i, int(a[0]) ** float(a[1]))
                   i = len(str(int(a[0]) ** float(a[1]))) + 1
               elif (a[0].find(".") != -1 and a[1].find(".") != -1):
                   ent.insert(i, float(a[0]) ** float(a[1]))
                   i = len(str(float(a[0]) ** float(a[1]))) + 1
   elif(op=="AC"):
        ent.delete(0,END)
   elif(op=="C"):
       if(len(ent.get()) == 1):
           ent.delete(0, END)
           return
       ent.delete(len(ent.get())-1, END)

ent = Entry(width=26,font="large_font",borderwidth=5,relief=SUNKEN)
ent.pack()
f1 = Frame(bg="gold",padx=36,pady=71,borderwidth=5,relief=SUNKEN)
f1.pack(anchor=N,side=TOP)
cal.wm_iconbitmap("Dtafalonso-Android-Lollipop-Calculator.ico")
i=0
ope=""
but = Button(f1,text="C",padx=11,pady=11,command=partial(calcu,"C"))
but.grid(row=2,column=0)
but = Button(f1,text="AC",padx=11,pady=11,command=partial(calcu,"AC"))
but.grid(row=2,column=1)
but = Button(f1,text="%",padx=11,pady=11,command=partial(calcu,"%"))
but.grid(row=2,column=2)
but = Button(f1,text="/",padx=10,pady=11,command=partial(calcu,"/"))
but.grid(row=2,column=3)
but = Button(f1,text=7,padx=12,pady=11,command=partial(calcu,7))
but.grid(row=3,column=0)
but = Button(f1,text=8,padx=16,pady=11,command=partial(calcu,8))
but.grid(row=3,column=1)
but = Button(f1,text=9,padx=13,pady=11,command=partial(calcu,9))
but.grid(row=3,column=2)
but = Button(f1,text="*",padx=10,pady=11,command=partial(calcu,"*"))
but.grid(row=3,column=3)
but = Button(f1,text=4,padx=12,pady=11,command=partial(calcu,4))
but.grid(row=4,column=0)
but = Button(f1,text=5,padx=16,pady=11,command=partial(calcu,5))
but.grid(row=4,column=1)
but = Button(f1,text=6,padx=13,pady=11,command=partial(calcu,6))
but.grid(row=4,column=2)
but = Button(f1,text="-",padx=10,pady=11,command=partial(calcu,"-"))
but.grid(row=4,column=3)
but = Button(f1,text=1,padx=12,pady=11,command=partial(calcu,1))
but.grid(row=5,column=0)
but = Button(f1,text=2,padx=16,pady=11,command=partial(calcu,2))
but.grid(row=5,column=1)
but = Button(f1,text=3,padx=13,pady=11,command=partial(calcu,3))
but.grid(row=5,column=2)
but = Button(f1,text="+",padx=9,pady=11,command=partial(calcu,"+"))
but.grid(row=5,column=3)
but = Button(f1,text="=",padx=11,pady=10,command=partial(calcu,"="))
but.grid(row=6,column=0)
but = Button(f1,text="^",padx=15,pady=10,command=partial(calcu,"^"))
but.grid(row=6,column=1)
but = Button(f1,text=0,padx=13,pady=10,command=partial(calcu,0))
but.grid(row=6,column=2)
but = Button(f1,text=".",font=("lucida 9 bold"),padx=12,pady=10,command=partial(calcu,"."))
but.grid(row=6,column=3)
cal.mainloop()