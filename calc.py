from tkinter import *
from math import * 
import tkinter.messagebox 

root = Tk()
root.title("Calculator")
root.resizable(0, 0)
root.geometry("420x400+0+0")
root.configure(background="chartreuse")

calc=Frame(root,bg="red")
calc.grid()

Label1= Label(calc, text = "SCIENTIFIC CALCULATOR",fg="navy blue",bg="powder blue",font=('arial',20,'bold','italic'))


equa = "" 
equation = StringVar()
calculation = Entry(calc, textvariable = equation,fg="green",font=('arial',15,'bold'),bg="powder blue",bd=20,width=34,justify=LEFT)
calculation.grid(row=0, columnspan=4,column=0,pady=1)
SUB = str.maketrans("013456789", "₀₁₃₄₅₆₇₈₉")
SUP = str.maketrans("013456789", "⁰¹³⁴⁵⁶⁷⁸⁹")


def percentage(x,y):
    z=(x/y)*100
    return z
def scf(x,y):
    k=-x/y
    return k
def acceleration(x,y):
    a=x/y
    return a
def velocity(x,y):
    a=x/y
    return a
def angularvelocity(x,y):
    w=x/y
    return w
def linearspeed(x,y):
    a=x*y
    return a
def torque(x,y):
    a=x*y
    return a
def power(x,y):
    a=x/y
    return a
def avg_acceleration(x,y,z):
    a=(x-y)/z
    return a
def ang_acceleration(x,z):
    a=x/z
    return a
def tension(x,y):
    a=x*9.8-x*y
    return a
def surfcechargedensity(x,y):
    a= x/y
    return a
def position(x,y):
    a=y-x
    return a
def energy_density(x,y):
    a=(1/2)*x*(y**2)
    b=1/2*x*(y**2)
    return a+b
def heatoffusion(x,y):
    a=x/y
    return a
def workgravity(x,y,z=1):
    a=x*y*9.8*z
    return a
def shear_mod(x,y,z,m):
    a=(x*y)/(z*m)
    return a
def magnaticflux(x,y,z,m):
    a=x*y*z*m
    return a
def g():
    a=9.8
    return a
def heatcapacity(x,y):
    a=x/y
    return a
def wavelength(x,y):
    a=x/y
    return a
def wavespeed(x,y):
    a=x*y
    return a
def deceleration(x,y,z):
    a=(x-y)/z
    return a
def intensity(x,y):
    a=x/y
    return a
def mechenergy(x,y,z):
    a=(1/2)*x*y**2+x*9.8*z
    return a
def tangentialvelocity(x,y):
    a=x/y
    return a
def chargedensity(x,y):
    a=x/y
    return a
    
def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
def EqualPress():
    global equa
    x=calculation.get()  
    if(equa==""):
               equa=equa+x              
    try:
               total = str(eval(equa))
               equation.set(total)
               if(float(total)==0):
                              equa=""
               else:
                              equa=total
    except:
               equation.set("ERROR")
               equa=""
               pass                                     
def ClearPress():
    global equa
    equa = ""
    equation.set("") 
Button0 = Button(calc, text="0", command = lambda:btnPress(0), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button0.grid(row = 7, column = 2, padx=10, pady=10)


Button1 = Button(calc, text="1", command = lambda:btnPress(1), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button1.grid(row = 3, column = 0, padx=10, pady=10)

Button14 = Button(calc, text="(", command = lambda:btnPress("("), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button14.grid(row = 6, column = 0, padx=10, pady=10)

Button2 = Button(calc, text="2", command = lambda:btnPress(2), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button2.grid(row = 3, column = 1, padx=10, pady=10)

Button3 = Button(calc, text="3", command = lambda:btnPress(3), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button3.grid(row = 3, column = 2, padx=10, pady=10)

Button13 = Button(calc, text="sqrt", command = lambda:btnPress("sqrt("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button13.grid(row = 5, column = 7, padx=10, pady=10)

Button21 = Button(calc, text="pow", command = lambda:btnPress("pow("), borderwidth=1,bd=4,width=6,height=1,bg="white",relief=SOLID,font=('arial',15,'bold'))
Button21.grid(row = 5, column = 5, padx=10, pady=10)

Button4 = Button(calc, text="4", command = lambda:btnPress(4), borderwidth=1,bd=4,width=6,height=1,bg="orange",relief=SOLID,font=('arial',15,'bold'))
Button4.grid(row = 4, column = 0, padx=10, pady=10)

Button15 = Button(calc, text=")", command = lambda:btnPress(")"), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button15.grid(row = 6, column = 1, padx=10, pady=10)
Button5 = Button(calc, text="5", command = lambda:btnPress(5), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button5.grid(row = 4, column = 1, padx=10, pady=10)
Button6 = Button(calc, text="6", command = lambda:btnPress(6), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button6.grid(row = 4, column = 2, padx=10, pady=10)
Button7 = Button(calc, text="7", command = lambda:btnPress(7), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button7.grid(row = 5, column = 0, padx=10, pady=10)
Button16 = Button(calc, text=".", command = lambda:btnPress("."), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button16.grid(row = 6, column = 2, padx=10, pady=10)
Button8 = Button(calc, text="8", command = lambda:btnPress(8), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button8.grid(row = 5, column = 1, padx=10, pady=10)
Button9 = Button(calc, text="9", command = lambda:btnPress(9), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button9.grid(row = 5, column = 2, padx=10, pady=10)
Plus = Button(calc, text="+", command = lambda:btnPress("+"), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Plus.grid(row = 3, column = 3, padx=10, pady=10)
Minus = Button(calc, text="-", command = lambda:btnPress("-"), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Minus.grid(row = 4, column = 3, padx=10, pady=10)
Button18 = Button(calc, text="sin", command = lambda:btnPress("sin("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button18.grid(row = 4, column = 4, padx=10, pady=10)

Button22 = Button(calc, text="log", command = lambda:btnPress("log("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button22.grid(row = 3, column = 4, padx=10, pady=10)

Multiply = Button(calc, text="x", command = lambda:btnPress("*"), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Multiply.grid(row = 5, column = 3, padx=10, pady=10)

Button19 = Button(calc, text="cos-1".translate(SUP), command = lambda:btnPress("cos("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button19.grid(row = 5, column = 4, padx=10, pady=10)

Button23 = Button(calc, text="pi", command = lambda:btnPress("pi"), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button23.grid(row = 5, column = 6, padx=10, pady=10)

Divide = Button(calc, text="/", command = lambda:btnPress("/"), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Divide.grid(row = 7, column = 3, padx=10, pady=10)

Button20 = Button(calc, text="factorial", command = lambda:btnPress("factorial("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button20.grid(row = 6, column = 4, padx=10, pady=10)

Button24 = Button(calc, text="comma", command = lambda:btnPress(","), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button24.grid(row = 8, column = 3, padx=10, pady=10)

Equal = Button(calc, text="=", command = EqualPress, borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Equal.grid(row=7, column=1, padx=10, pady=10)

Clear = Button(calc, text="CLEAR", command = ClearPress, borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Clear.grid(row = 7, column = 0, padx=10, pady=10)

Button17 = Button(calc, text="remainder", command = lambda:btnPress("%"), borderwidth=1,bd=4,width=8,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button17.grid(row = 9, column = 5, padx=17, pady=10)

Button25 = Button(calc, text="degrees", command = lambda:btnPress("degrees("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button25.grid(row = 3, column = 5, padx=10, pady=10)

Button26 = Button(calc, text="log10", command = lambda:btnPress("log10("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button26.grid(row = 3, column = 6, padx=10, pady=10)

Button27 = Button(calc, text="log1p", command = lambda:btnPress("log1p("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button27.grid(row = 3, column = 7, padx=10, pady=10)

Button28 = Button(calc, text="radians", command = lambda:btnPress("radians("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button28.grid(row = 4, column = 5, padx=10, pady=10)

Button29 = Button(calc, text="sinh", command = lambda:btnPress("sinh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button29.grid(row = 4, column = 6, padx=10, pady=10)
  

Button30 = Button(calc, text="cosh", command = lambda:btnPress("cosh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button30.grid(row = 4, column = 7, padx=10, pady=10)

Button31 = Button(calc, text="tan", command = lambda:btnPress("tan("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button31.grid(row = 6, column = 6, padx=10, pady=10)

Button32 = Button(calc, text="tanh", command = lambda:btnPress("tanh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button32.grid(row = 6, column = 7, padx=10, pady=10)

Button33 = Button(calc, text="E", command = lambda:btnPress("e"), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button33.grid(row = 7, column = 4, padx=10, pady=10)

Button34 = Button(calc, text="tan-1".translate(SUP), command = lambda:btnPress("atan("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button34.grid(row = 7, column = 6, padx=10, pady=10)


Button35 = Button(calc, text="gcd", command = lambda:btnPress("gcd("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button35.grid(row = 6, column = 5, padx=10, pady=10)

Button36 = Button(calc, text="exp", command = lambda:btnPress("exp("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button36.grid(row = 7, column = 5, padx=10, pady=10)

Button37 = Button(calc, text="lgamma", command = lambda:btnPress("lgamma("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button37.grid(row = 7, column = 7, padx=10, pady=10)

Button38 = Button(calc, text="sin-1".translate(SUP), command = lambda:btnPress("asin("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button38.grid(row = 8, column = 4, padx=10, pady=10)

Button39 = Button(calc, text="cos-1".translate(SUP), command = lambda:btnPress("acos("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button39.grid(row = 8, column = 5, padx=10, pady=10)

Button40 = Button(calc, text="tan2-1 ".translate(SUP), command = lambda:btnPress("atan2("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button40.grid(row = 8, column = 6, padx=10, pady=10)

Button41 = Button(calc, text="hypot", command = lambda:btnPress("hypot("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button41.grid(row = 8, column = 7, padx=10, pady=10)


Button42 = Button(calc, text="cosh-1".translate(SUP), command = lambda:btnPress("acosh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button42.grid(row = 10, column = 0, padx=10, pady=10)

Button43 = Button(calc, text="sinh-1".translate(SUP), command = lambda:btnPress("asinh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button43.grid(row = 10, column = 1, padx=10, pady=10)

Button44 = Button(calc, text="tanh-1".translate(SUP), command = lambda:btnPress("atanh("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button44.grid(row = 9, column = 6, padx=10, pady=10)

Button45 = Button(calc, text="gamma", command = lambda:btnPress("gamma("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button45.grid(row = 9, column = 7, padx=10, pady=10)


Button46 = Button(calc, text="ceil", command = lambda:btnPress("ceil("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button46.grid(row = 10, column = 4, padx=10, pady=10)


Button47 = Button(calc, text="floor", command = lambda:btnPress("floor("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button47.grid(row = 9, column = 4, padx=10, pady=10)

Button48 = Button(calc, text="expm1", command = lambda:btnPress("expm1("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button48.grid(row = 9, column = 2, padx=10, pady=10)

Button49 = Button(calc, text="abs", command = lambda:btnPress("abs("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button49.grid(row = 9, column = 3, padx=10, pady=10)

Button50 = Button(calc, text="int", command = lambda:btnPress("int("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button50.grid(row = 8, column = 1, padx=10, pady=10)

Button51 = Button(calc, text="float", command = lambda:btnPress("float("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button51.grid(row = 8, column = 2, padx=10, pady=10)

Button52 = Button(calc, text="fsum", command = lambda:btnPress("fsum("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button52.grid(row = 8, column = 0, padx=10, pady=10)

Button53 = Button(calc, text="frexp", command = lambda:btnPress("frexp("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button53.grid(row = 9, column = 0, padx=10, pady=10)

Button54 = Button(calc, text="ldexp", command = lambda:btnPress("ldexp("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button54.grid(row = 9, column = 1, padx=10, pady=10)


Button55 = Button(calc, text="trunc", command = lambda:btnPress("trunc("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button55.grid(row = 10, column = 3, padx=10, pady=10)

Button56 = Button(calc, text="modf", command = lambda:btnPress("modf("), borderwidth=1,bd=4,width=6,height=1,bg="white", relief=SOLID,font=('arial',15,'bold'))
Button56.grid(row = 10, column = 2, padx=10, pady=10)

Button57 = Button(calc, text="%", command = lambda:btnPress("percentage("), borderwidth=1,bd=4,width=6,height=1,bg="orange", relief=SOLID,font=('arial',15,'bold'))
Button57.grid(row = 6, column = 3, padx=10, pady=10)

Button58 = Button(calc, text="spring c", command = lambda:btnPress("scf("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button58.grid(row = 11, column = 0, padx=10, pady=10)

Button60 = Button(calc, text="velocity", command = lambda:btnPress("velocity("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button60.grid(row = 11, column = 2, padx=10, pady=10)
Button59 = Button(calc, text="acc", command = lambda:btnPress("acceleration("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button59.grid(row = 11, column = 1, padx=10, pady=10)

Button61 = Button(calc, text="ang vel", command = lambda:btnPress("angvel("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button61.grid(row = 11, column = 3, padx=10, pady=10)

Button62 = Button(calc, text="magflux", command = lambda:btnPress("magnaticflux("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button62.grid(row = 11, column = 4, padx=10, pady=10)

Button63 = Button(calc, text="torque", command = lambda:btnPress("torque("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button63.grid(row = 11, column = 5, padx=10, pady=10)

Button64 = Button(calc, text="power", command = lambda:btnPress("power("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button64.grid(row = 11, column = 6, padx=10, pady=10)

Button67 = Button(calc, text="avg acc", command = lambda:btnPress("avg_acceleration("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button67.grid(row = 11, column = 7, padx=10, pady=10)

Button68 = Button(calc, text="ang acc", command = lambda:btnPress("ang acceleration("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button68.grid(row = 11, column = 8, padx=10, pady=10)

Button69 = Button(calc, text="tension", command = lambda:btnPress("tension("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button69.grid(row = 10, column = 8, padx=10, pady=10)

Button70 = Button(calc, text="scd", command = lambda:btnPress("surfacechargedensity("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button70.grid(row = 9, column = 8, padx=1, pady=10)

Button71 = Button(calc, text="wavelen", command = lambda:btnPress("wavelength("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button71.grid(row = 8, column = 8, padx=1, pady=1)

Button72 = Button(calc, text="edensity", command = lambda:btnPress("energy_density("), borderwidth=1,bd=4,width=10,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button72.grid(row = 7, column = 8, padx=1, pady=1)

Button73 = Button(calc, text="fusion", command = lambda:btnPress("hetoffusion("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button73.grid(row = 6, column = 8, padx=1, pady=1)

Button74 = Button(calc, text="work(g)", command = lambda:btnPress("workgravity("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button74.grid(row = 5, column = 8, padx=1, pady=1)

Button75 = Button(calc, text="shearmod", command = lambda:btnPress("shear_mod("), borderwidth=1,bd=4,width=10,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button75.grid(row = 4, column = 8, padx=1, pady=1)

Button76 = Button(calc, text="deacc", command = lambda:btnPress("deceleration("), borderwidth=1,bd=4,width=6,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button76.grid(row = 3, column = 8, padx=1, pady=1)

Button77 = Button(calc, text="g", command = lambda:btnPress("g()"), borderwidth=1,bd=4,width=7,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button77.grid(row = 10, column = 6, padx=1, pady=1)

Button78 = Button(calc, text="wavespeed", command = lambda:btnPress("wavespeed("), borderwidth=1,bd=4,width=9,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button78.grid(row = 10, column = 7, padx=1, pady=1)

Button79 = Button(calc, text="mecherg", command = lambda:btnPress("mechenergy("), borderwidth=1,bd=4,width=9,height=1,bg="green", relief=SOLID,font=('arial',15,'bold'))
Button79.grid(row = 10, column = 5, padx=1, pady=1)

def exit():
  exit=tkinter.messagebox.askyesno('scientific calculator',"confirm if you want to exit")
  if exit>0:
    root.destroy()
    return
def scientific():
    root.resizable(width=False, height=False)
    root.geometry("905x590+0+0")

def standard():
  root.resizable(width=False,height=False)
  root.geometry("420x400+0+0")

def physical():
    root.resizable(width=False, height=False)
    root.geometry("1310x660+0+0")

menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="standard",command=standard)
filemenu.add_command(label="scientific",command=scientific)
filemenu.add_command(label="physics",command=physical)
filemenu.add_separator()
filemenu.add_command(label="exit",command=exit)

root.config(menu=menubar)
root.mainloop()
