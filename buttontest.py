from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('PKalculator')
root.resizable(width=False, height=False)
root.iconbitmap('./PKicon.ico')
bgcolor = '#161C2D'
fcolor = '#D1D3DF'
buttonscolor = '#1A2136'
root.configure(bg=bgcolor)
# ------------------- Buttons ----------------------
btn_del = Button(root, text="\u2326", width=10, height=2, bg=buttonscolor, fg=fcolor)
btn_del.place(x=10, y=350)

root.mainloop()
