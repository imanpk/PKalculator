from tkinter import *
import tkinter.messagebox

# ========================== SETTINGS ========================
root = Tk()
root.geometry('400x400')
root.title('PKalculator')
root.resizable(width=False, height=False)
root.iconbitmap('./PKicon.ico')
bgcolor = '#161C2D'
fcolor = '#D1D3DF'
buttonscolor = '#1A2136'
root.configure(bg=bgcolor)

# ========================== VARIABLES ==========================
total = float()
current = float()
input_value = ''
# num1 = StringVar()
# num2 = StringVar()
# resultvar = StringVar()
# inputvals = ''
equations = ''
last_used_func = ''
# tempvalue = ''

# ========================== FRAMES ==========================
top_first = Frame(root, width=400, height=70, bg=bgcolor)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=70, bg=bgcolor)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=260, bg=bgcolor)
top_third.pack(side=BOTTOM)


# ========================== FUNCTIONS ==========================

def insertnum(text):
    global input_value
    global equations
    input_value = input_value + str(text)
    equations = equations + str(text)
    display.set(input_value)
    equation.set(equations)


def backspace():
    global input_value
    input_value = input_value[:-1]
    display.set(input_value)


def clear():
    global total, equations, current, input_value
    input_value = ""
    equations = ''
    total = 0
    current = 0
    display.set(input_value)
    equation.set(input_value)


def errorMsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error', 'Something went wrong!!')


def plus():
    try:
        global total, equations, current, input_value, last_used_func
        input_value = ''
        current = float(display.get())
        total += current
        current = 0
        display.set(total)
        equations = equations + str('+')
        equation.set(equations)
        last_used_func = 'plus'
    except:
        errorMsg('error')


def minus():
    try:
        global total, equations, current, input_value, last_used_func
        input_value = ''
        current = float(display.get())
        if total != 0:
            total -= current
        else:
            total = current
        current = 0
        display.set(total)
        equations = equations + str('-')
        equation.set(equations)
        last_used_func = 'minus'
    except:
        errorMsg('error')


def multiply():
    try:
        global total, equations, current, input_value, last_used_func
        input_value = ''
        current = float(display.get())
        if total != 0:
            total *= current
        else:
            total = current
        current = 0
        display.set(total)
        equations = equations + str('*')
        equation.set(equations)
        last_used_func = 'multiply'
    except:
        errorMsg('error')


def divide():
    try:
        global total, equations, current, input_value, last_used_func
        input_value = ''
        current = float(display.get())
        if total != 0:
            total /= current
        else:
            total = current
        current = 0
        display.set(total)
        equations = equations + str('/')
        equation.set(equations)
        last_used_func = 'divide'
    except:
        errorMsg('error')


def eq():
    global total, equations, current, input_value, last_used_func
    if last_used_func == 'plus':
        current = float(display.get())
        total += current
    elif last_used_func == 'minus':
        current = float(display.get())
        total -= current
    elif last_used_func == 'multiply':
        current = float(display.get())
        total *= current
    elif last_used_func == 'divide':
        current = float(display.get())
        total /= current
    input_value = ''
    display.set(total)
    current = float(display.get())
    equations = equations + str('=')
    equation.set(equations)


# ========================== Buttons ==========================
btn_0 = Button(top_third, text="0", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('0'))
btn_0.place(x=105, y=210)

btn_1 = Button(top_third, text="1", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('1'))
btn_1.place(x=10, y=160)

btn_2 = Button(top_third, text="2", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('2'))
btn_2.place(x=105, y=160)

btn_3 = Button(top_third, text="3", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('3'))
btn_3.place(x=200, y=160)

btn_4 = Button(top_third, text="4", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('4'))
btn_4.place(x=10, y=110)

btn_5 = Button(top_third, text="5", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('5'))
btn_5.place(x=105, y=110)

btn_6 = Button(top_third, text="6", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('6'))
btn_6.place(x=200, y=110)

btn_7 = Button(top_third, text="7", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('7'))
btn_7.place(x=10, y=60)

btn_8 = Button(top_third, text="8", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('8'))
btn_8.place(x=105, y=60)

btn_9 = Button(top_third, text="9", width=11, height=2, bg=buttonscolor, fg=fcolor,
               command=lambda: insertnum('9'))
btn_9.place(x=200, y=60)

btn_dot = Button(top_third, text=".", width=11, height=2, bg=buttonscolor, fg=fcolor,
                 command=lambda: insertnum('.'))
btn_dot.place(x=200, y=210)

btn_eq = Button(top_third, text="=", width=11, height=2, bg=buttonscolor, fg=fcolor,
                command=lambda: eq())
btn_eq.place(x=295, y=210)

btn_plus = Button(top_third, text="+", width=11, height=2, bg=buttonscolor, fg=fcolor,
                  command=lambda: plus())
btn_plus.place(x=295, y=160)

btn_minus = Button(top_third, text="-", width=11, height=2, bg=buttonscolor, fg=fcolor,
                   command=lambda: minus())
btn_minus.place(x=295, y=110)

btn_mul = Button(top_third, text="*", width=11, height=2, bg=buttonscolor, fg=fcolor,
                 command=lambda: multiply())
btn_mul.place(x=295, y=60)

btn_div = Button(top_third, text="/", width=11, height=2, bg=buttonscolor, fg=fcolor,
                 command=lambda: divide())
btn_div.place(x=295, y=10)

btn_sqrt = Button(top_third, text="√", width=11, height=2, bg=buttonscolor, fg=fcolor,
                  command=lambda: insertnum('√'))
btn_sqrt.place(x=200, y=10)

btn_sqr2 = Button(top_third, text="y2", width=11, height=2, bg=buttonscolor, fg=fcolor,
                  command=lambda: insertnum('y2'))
btn_sqr2.place(x=105, y=10)

btn_clr = Button(top_third, text="C", width=11, height=2, bg=buttonscolor, fg=fcolor,
                 command=lambda: clear())
btn_clr.place(x=10, y=10)

btn_del = Button(top_third, text="\u2326", width=11, height=2, bg=buttonscolor, fg=fcolor,
                 command=lambda: backspace())
btn_del.place(x=10, y=210)
# ========================== Entries and Labels ==========================

# label_first_num = Label(top_first, text='Computation: ', bg=bgcolor, fg=fcolor, font=("Cascadia Code", 14))
# label_first_num.pack(side=LEFT, pady=10, padx=10)

display = StringVar()
equation = StringVar()
operations = Entry(top_first, bg=bgcolor, textvariable=equation, fg=fcolor,
                   font=("Cascadia Code", 14))
operations.place(x=10, y=10, width=380, height=50)

# label_second_num = Label(top_second, text='Inputs: ', bg=bgcolor, fg=fcolor,
#                          font=("Cascadia Code", 14))
# label_second_num.pack(side=LEFT, pady=10, padx=10)

inputs = Entry(top_second, bg=bgcolor, textvariable=display, fg=fcolor,
               font=("Cascadia Code", 14))
inputs.place(x=10, y=10, width=380, height=50)

# res = Label(top_first, text='Result: ', bg=bgcolor, fg=fcolor, font=("Cascadia Code", 14))
# res.pack(side=LEFT, pady=10, padx=10)

# res_num = Entry(top_first, highlightbackground=bgcolor, textvariable=resultvar)
# res_num.pack(side=LEFT)
# ===================================================================================
root.mainloop()
