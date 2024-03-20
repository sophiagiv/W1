from tkinter import *
from tkmacosx import Button 

root = Tk()
root.title("Calculator App")
root.configure(background="Goldenrod") 
root.geometry ("500x300")

label = Label(root, text='', padx = 10, pady = 10, background = 'khaki3', fg ='linen')
label.grid(row = 0, columnspan = 4, sticky = EW)

equation = ""

def show_button(value):
    global equation
    equation += value 
    label.config(text = equation)

#equal      
def equal_sign(): 
    global equation
    try:
        result = eval(equation)
        label.config(text= result)
        equation = str(result)
    except ZeroDivisionError:
        label.config(text = "Error; not a number ")
button_equal = Button(root, text = "=", command=equal_sign, pady = 10, padx = 10, background = 'linen', fg ='chocolate')
button_equal.grid(row=5, column=2,)

#percent
def percent_sign():
    global equation
    if equation != "":
        try:
            result = str(eval(equation) / 100)
            label.config(text = result)
        except Exception:
            label.config(text= "Error; ")
        else: #remove one tab before else, to align it with the above if. Current function will return an error. -2 points
            label.config(text="error; no num ")
button_percent = Button(root, text='%', command=percent_sign, padx=10, pady=10, background='linen', fg='chocolate')
button_percent.grid(row=6, column=0)

# missing a negate symbol, to allow a shortcut for any negation operation. -8 points.

#clear 
def clear_button():
    global equation
    equation = ""
    label.config(text = 0)

button_clear = Button(root, text='C', command=clear_button, padx=10, pady=10, background='linen', fg='chocolate')
button_clear.grid(row=5, column=0)

#divide button 
def divide_num():
    global equation
    equation += '/'
    label.config(text=equation)

button_divide = Button(root, text = "/", command=divide_num, pady = 10, padx = 10, background = 'linen', fg ='chocolate')
button_divide.grid(row=5, column=3)

#multiply
def multiply_num():
    global equation
    equation += '*'
    label.config(text=equation)
button_multiply = Button(root, text = "*", command=multiply_num,pady = 10, padx = 10,background = 'linen', fg ='chocolate')
button_multiply.grid(row=4, column=3, )
#sub 
def subtract_num():
    global equation
    equation += '-'
    label.config(text=equation)
button_subtract = Button(root, text='-', command=subtract_num, padx=10, pady=10, background='linen', fg='chocolate')
button_subtract.grid(row=3, column=3)

#add
def add_num():
    global equation
    equation += '+'
    label.config(text=equation)
button_add = Button(root, text = "+", command=add_num, pady = 10, padx = 10,background = 'linen', fg ='chocolate')
button_add.grid(row=2, column=3,)

#numbers 

#0
button_0 = Button(root, text='0', command=lambda: show_button('0'), padx=10, pady=10, background='linen', fg='chocolate')
button_0.grid(row=5, column=1)

#1. 
button_1 = Button(root, text='1', command=lambda: show_button('1'), padx=10, pady=10, background='linen', fg='chocolate')
button_1.grid(row=2, column=0)
#2
button_2 = Button(root, text='2', command=lambda: show_button('2'), padx=10, pady=10, background='linen', fg='chocolate')
button_2.grid(row=2, column=1)

#3
button_3 = Button(root, text='3', command=lambda: show_button('3'), padx=10, pady=10, background='linen', fg='chocolate')
button_3.grid(row=2, column=2)

#4
button_4 = Button(root, text='4', command=lambda: show_button('4'), padx=10, pady=10, background='linen', fg='chocolate')
button_4.grid(row=3, column=0)

#5
button_5 = Button(root, text='5', command=lambda: show_button('5'), padx=10, pady=10, background='linen', fg='chocolate')
button_5.grid(row=3, column=1)

button_6 = Button(root, text='6', command=lambda: show_button('6'), padx=10, pady=10, background='linen', fg='chocolate')
button_6.grid(row=3, column=2)

#7
button_7 = Button(root, text='7', command=lambda: show_button('7'), padx=10, pady=10, background='linen', fg='chocolate')
button_7.grid(row=4, column=0)

#8
button_8 = Button(root, text='8', command=lambda: show_button('8'), padx=10, pady=10, background='linen', fg='chocolate')
button_8.grid(row=4, column=1)

#9
button_9 = Button(root, text='9', command=lambda: show_button('9'), padx=10, pady=10, background='linen', fg='chocolate')
button_9.grid(row=4, column=2)

root.mainloop()
