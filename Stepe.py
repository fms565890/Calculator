from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x360")
root.config(bg="")
root.resizable(False ,False)

def max():
    num = ro.get()
    
    ad = Label(root ,text="")
    ad.grid(row=0 ,column=2)
    if len(num) == 10:
        ad.config(text="بیشتر از 10")
        ro.delete(0 ,END)
        ro.insert(0 ,num)

    num = ro.get()   
    if len(num) < 10:
        
        ad.config(text="               ")

def btn(test ,command ,row ,colume ,bg):
    btn = Button(fr ,text=test ,command=command ,width=6 ,height=1 ,padx=20 ,pady=20 ,bg=bg)
    btn.grid(row=row ,column=colume)


def number(number):
    
    num = ro.get()


    
    if len(num) == 10:
        max()

    elif len(num) < 10:

        
        s = num + str(number)
        ro.delete(0 ,END)
        ro.insert(0 ,s)


def oper(o):
    
    r = ro.get()


    if len(r) == 10:
        max()

    elif len(r) < 10:
        op = r + str(o)
        ro.delete(0 ,END)
        ro.insert(0 ,op)
    

def eq():
    
    e = ro.get()


    if len(e) == 10:
        max()

    elif len(e) < 10:
        ro.delete(0 ,END)
        try:
            a = eval(e) 
        except:
            a = "Error"

    ro.insert(0 , a)

def clear():
    
    a = ro.get()

    ro.delete(0 ,END)

    if len(a) == 10:
        max()

    elif len(a) < 10:

        ro.delete(0 ,END)

ro = Entry(root , font=("none" ,26))
ro.grid(row=0 ,columnspan=3 ,padx=10 ,pady=10)

fr = Frame(height=20 ,bg="blue")
fr.grid(row=1 ,columnspan=3)
# 1 - 2 - 3
btn(test=1 , command= lambda:number(1) ,row=2 ,colume=0 ,bg="white")
btn(test=2 , command= lambda:number(2) ,row=2 ,colume=1 ,bg="white")
btn(test=3 , command= lambda:number(3) ,row=2 ,colume=2 ,bg="white")
# 4 - 5 - 6
btn(test=4 , command= lambda:number(4) ,row=3 ,colume=0 ,bg="white")
btn(test=5 , command= lambda:number(5) ,row=3 ,colume=1 ,bg="white")
btn(test=6 , command= lambda:number(6) ,row=3 ,colume=2 ,bg="white")
# 7 - 8 - 9
btn(test=7 , command= lambda:number(7) ,row=4 ,colume=0 ,bg="white")
btn(test=8 , command= lambda:number(8) ,row=4 ,colume=1 ,bg="white")
btn(test=9 , command= lambda:number(9) ,row=4 ,colume=2 ,bg="white")
# C - 0 - =
btn(test="C" ,command= lambda : clear() ,row=5 ,colume=0 ,bg="red")
btn(test=0 , command= lambda:number(0) ,row=5 ,colume=1 ,bg="white")
btn(test="=" ,command= lambda : eq() ,row=5 ,colume=2 ,bg="green")
# + _ - _ * _ /
btn(test="/" ,command= lambda : oper("/") ,row=2 ,colume=4 ,bg="white")
btn(test="*" ,command= lambda : oper("*") ,row=3 ,colume=4 ,bg="white")
btn(test="-" ,command= lambda : oper("-") ,row=4 ,colume=4 ,bg="white")
btn(test="+" ,command= lambda : oper("+") ,row=5 ,colume=4 ,bg="white")




root.mainloop()
