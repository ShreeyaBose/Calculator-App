from tkinter import *

gui = Tk()
gui.title("Simple Calculator")
gui.geometry("570x600+100+200")
gui.resizable(0,0)
gui.configure(bg="#17161b")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result = Label(gui, width=25, height=2, text="", font=("arial",30))
label_result.pack()
    
btn1=Button(gui,text="c",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear())
btn1.place(x=10,y=100)
btn2=Button(gui,text="/",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/"))
btn2.place(x=150,y=100)
btn3=Button(gui,text="%",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%"))
btn3.place(x=290,y=100)
btn4=Button(gui,text="*",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*"))
btn4.place(x=430,y=100)
    
btn5=Button(gui,text="7",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7"))
btn5.place(x=10,y=200)
btn6=Button(gui,text="8",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8"))
btn6.place(x=150,y=200)
btn7=Button(gui,text="9",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9"))
btn7.place(x=290,y=200)
btn8=Button(gui,text="-",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-"))
btn8.place(x=430,y=200)

btn9=Button(gui,text="4",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4"))
btn9.place(x=10,y=300)
btn10=Button(gui,text="5",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5"))
btn10.place(x=150,y=300)
btn11=Button(gui,text="6",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6"))
btn11.place(x=290,y=300)
btn12=Button(gui,text="+",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+"))
btn12.place(x=430,y=300)

btn13=Button(gui,text="1",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1"))
btn13.place(x=10,y=400)
btn14=Button(gui,text="2",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2"))
btn14.place(x=150,y=400)
btn15=Button(gui,text="3",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3"))
btn15.place(x=290,y=400)
btn16=Button(gui,text="0",width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0"))
btn16.place(x=10,y=500)

btn17=Button(gui,text=".",width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("."))
btn17.place(x=290,y=500)
btn18=Button(gui,text="=",width=5, height=3, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate())
btn18.place(x=430,y=400)


gui.mainloop()
