from tkinter import *
from tkinter import ttk
import pyautogui
print(pyautogui.size())

w, h= pyautogui.size()

flavours={
    'Apple':1.25, 'Bubblegum':1.30, 'Butterscotch':1.20, 'Chocolate':1.25, 'Jamum':1.30, 'Vanilla':1.25
}

size={
    'cup(1 serving)':1.0, 'cone(2 servings)':2.0, 'tub(4 servings)':4.0
}

toppings={
    'flake':0.30, 'strawberry sauce':0.10, 'chocolate sauce':0.10
    }

root= Tk()
root.title('Velvet Cream')
root.geometry(f'{w}x{h}')
Label(root, text= 'Welcome to Velvet Cream').place(x= w//3+200, y= 45)
frame= Frame(root, bg= '#7F2A3C').pack(pady= 15, padx= 5)
#flavours
Label(frame, text= 'Select your favourite ice cream flavour:').pack(pady= 10)
flavour= StringVar(value= list(flavours.keys())[0])
fla_list= ttk.Combobox(frame, textvariable= flavour, values= list(flavours.keys()), state= 'readonly').pack(pady=10)
#fla_list.current(0)
#size
Label(frame, text= 'Select your ice cream size:').pack(pady= 10)
size_variable= StringVar(value= list(size.keys())[0])
size_frame=Frame(frame)
size_frame.pack(pady= 10)
for i in size.keys():
    Radiobutton(size_frame, text= i, value= 1, variable= size_variable).pack(pady=2, )
#size_list= ttk.Combobox(frame, textvariable= size_variable, values= list(size.keys()), state= 'readonly').pack(pady=10)
#quantity

Label(frame, text= 'Select your quantity:').pack(pady= 10)
quantity_variable= StringVar(value= 1)
quantity_list= Spinbox(frame, textvariable= quantity_variable, from_= 1, to= 20).pack(pady=10)


root.mainloop()