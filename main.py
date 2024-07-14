

#lambda function:
# add = lambda x,y: x+y
#
# print(add(5,3))

#libraries
# GUI  Tkinker PyQt5

#Tkinter

# from tkinter import *
#
# root = Tk()
#
#
# #funtion
# def myclick():
#     hello = 'Hello'+ e.get()
#     my_label = Label(root,text=hello)
#     my_label.pack()
#
#
# #add label in our program
# my_label = Label(root,text='Hello! Please write your name')
# #to show label on screen
# my_label.pack()
#
# #input field
# e = Entry(root, width=100)
# e.pack()
#
# #add button
# my_button = Button(root,text='Click me',command=myclick, padx=20,pady=20,fg='Red',bg='Yellow')
# #to show buttonon screen
# my_button.pack()
#
#
# root.mainloop()

# GUI based calculator

from tkinter import *

root = Tk()
root.title('Calculator')

#add entry box
my_entry = Entry(root, width=50, borderwidth=10)
#my_entry.pack()
#my_button1 = Button(root,text='1',)
my_entry.grid(row=0,column=1, columnspan=3,padx=10,pady=20)

def button_click(number):
    current = my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,current+str(number))

def button_add():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Adition'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_sub():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Subtraction'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_mul():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Multiplication'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_div():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Division'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_equal():
    second_number =my_entry.get()
    s_num=int(second_number)
    my_entry.delete(0,END)
    if math == 'Addition':
        my_entry.insert(0,f_num+s_num)
    if math == 'Subtraction':
        my_entry.insert(0, f_num-s_num)
    if math == 'Multiplication':
        my_entry.insert(0, f_num*s_num)
    if math == 'Division':
        my_entry.insert(0, f_num/s_num)


#create button
my_button1 = Button(root,text='1',padx=40,pady=30,command=lambda: button_click(1))
my_button2 = Button(root,text='2',padx=40,pady=30,command=lambda: button_click(2))
my_button3 = Button(root,text='3',padx=40,pady=30,command=lambda: button_click(3))
my_button4 = Button(root,text='4',padx=40,pady=30,command=lambda: button_click(4))
my_button5 = Button(root,text='5',padx=40,pady=30,command=lambda: button_click(5))
my_button6 = Button(root,text='6',padx=40,pady=30,command=lambda: button_click(6))
my_button7 = Button(root,text='7',padx=40,pady=30,command=lambda: button_click(7))
my_button8 = Button(root,text='8',padx=40,pady=30,command=lambda: button_click(8))
my_button9 = Button(root,text='9',padx=40,pady=30,command=lambda: button_click(9))
my_button0 = Button(root,text='0',padx=40,pady=30,command=lambda: button_click(0))
my_button_Add = Button(root,text='+',padx=40,pady=30,command= button_add)
my_button_Sub = Button(root,text='-',padx=40,pady=30,command= button_sub)
my_button_Mul = Button(root,text='*',padx=40,pady=30,command= button_mul)
my_button_Div = Button(root,text='/',padx=40,pady=30,command= button_div)
my_button_Clear = Button(root,text='C',padx=40,pady=30,command=lambda: my_entry.delete(0,END))
my_button_Equals = Button(root,text='=',padx=40,pady=30,command=button_equal)


#button positioning
my_button7.grid(row=1,column=0)
my_button8.grid(row=1,column=1)
my_button9.grid(row=1,column=2)

my_button4.grid(row=2,column=0)
my_button5.grid(row=2,column=1)
my_button6.grid(row=2,column=2)

my_button1.grid(row=3,column=0)
my_button2.grid(row=3,column=1)
my_button3.grid(row=3,column=2)

my_button0.grid(row=4,column=1)

my_button_Add.grid(row=1,column=3)
my_button_Sub.grid(row=2,column=3)
my_button_Mul.grid(row=3,column=3)
my_button_Div.grid(row=4,column=3)

my_button_Clear.grid(row=4,column=0)
my_button_Equals.grid(row=4,column=2)


root.mainloop()












