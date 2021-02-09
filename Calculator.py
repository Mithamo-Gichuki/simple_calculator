# Importing modules
from tkinter import *
from math import sqrt
import math

# Screen creation
calc = Tk()
# Screen Title
calc.title('Simple Calculator')
# Logo / icon
# calc.iconbitmap()
calc.geometry('215x300')

# Functions section
# Function for number buttons click
global operator_list
operator_list = ['+', '-', '*', '/', '%', 'del', 'ce', 'c', 'sqrt', 'reciprocal']


def number_button_click(value):
    global num_val
    num_val = value
    current = calc_text_box.get()
    calc_text_box.delete(0, END)
    calc_text_box.insert(0, str(current) + str(value))


# Functions for operators


def operator_click(operator_val):
    global first_val
    first_val = int(calc_text_box.get())
    calc_text_box.delete(0, END)
    global btn_val
    btn_val = operator_val
    global display_operator
    display_operator = ''
    calc_text_box.delete(0, END)

    if btn_val == 'add':
        display_operator = '+'
    elif btn_val == 'subtract':
        display_operator = '-'
    elif btn_val == 'multiply':
        display_operator = 'x'
    elif btn_val == 'divide':
        display_operator = '/'
    elif btn_val == 'modulus':
        display_operator = '%'
    elif btn_val == 'reciprocal':
        display_operator = '1/x'
    elif btn_val == 'sqrt':
        display_operator = 'sqrt'
    elif btn_val == '+-':
        display_operator = '+-'

    calc_text_box.insert(0, str(first_val) + display_operator)


def equals_click():
    calc_text_box.delete(0, END)
    current_1 = calc_text_box.get()
    calc_text_box.delete(0, END)
    calc_text_box.insert(0, str(current_1) + str(num_val))
    second_val = int(calc_text_box.get())
    total_val = 0
    if btn_val == 'add':
        calc_text_box.delete(0, END)
        total_val = int(first_val + second_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '= \n' + str(total_val))
    elif btn_val == 'subtract':
        calc_text_box.delete(0, END)
        total_val = int(first_val - second_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))
    elif btn_val == 'multiply':
        calc_text_box.delete(0, END)
        total_val = int(first_val * second_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))
    elif btn_val == 'divide':
        calc_text_box.delete(0, END)
        total_val = int(first_val) / int(second_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))
    elif btn_val == 'modulus':
        calc_text_box.delete(0, END)
        total_val = int(first_val % second_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))
    elif btn_val == 'reciprocal':
        calc_text_box.delete(0, END)
        total_val = 1 / int(first_val)
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))
    elif btn_val == 'sqrt':
        calc_text_box.delete(0, END)
        total_val = sqrt(int(first_val))
        calc_text_box.insert(0, str(first_val) + display_operator + str(second_val) + '=' + str(total_val))


def delete(del_val):
    txt_get = calc_text_box.get()
    split_txt_get = ''
    txt_get_list = []
    for txt in txt_get:
        txt_get_list.append(txt)
    print('txt_get_list: ', txt_get_list)     # Debug list values
    print('txt_get: ', txt_get)
    print('txt_get type: ', type(txt_get))    # Debug output on console
    calc_text_box.delete(0, END)
    txt_to_operator = ''
    for txt in txt_get_list:
        if txt in operator_list:
            print('txt: ', txt)
            txt_to_operator = txt
            split_txt_get = txt_get.split(txt)
            print('split_txt_get: ', split_txt_get)
            if del_val == 'del':
                txt_get_list.pop()
                calc_text_box.insert(0, txt_get_list)
            elif del_val == 'ce':
                calc_text_box.delete(0, END)
            elif del_val == 'c':
                split_txt_get.pop()
                disp_val = split_txt_get[0] + txt_to_operator
                calc_text_box.insert(0, disp_val)
    print('txt_to_operator: ', txt_to_operator)
    """"
    calc_text_box.insert(0, txt_get[0: -1])
    txt_bx_val = calc_text_box.get()
    txt_bx_val_list = []
    

    print(txt_bx_val_list)
    """


# Text Box
# Row 0
calc_text_box = Entry(calc, width=35, bg='#e6e6ff')
calc_text_box.grid(row=0, column=0, columnspan=5, ipady=20, sticky='nsew')

# Buttons
# Row 1
delete_btn = Button(calc, text='DEL', command=lambda: delete('del'), bg='#99FFFF')
delete_btn.grid(row=1, column=0, sticky='nsew')
ce_btn = Button(calc, text='CE', command=lambda: delete('ce'), bg='#99FFFF')
ce_btn.grid(row=1, column=1, sticky='nsew')
c_btn = Button(calc, text='C', command=lambda: delete('c'), bg='#99FFFF')
c_btn.grid(row=1, column=2, sticky='nsew')
plus_minus_btn = Button(calc, text='+-', command=lambda: operator_click('+-'), bg='#99FFFF')
plus_minus_btn.grid(row=1, column=3, sticky='nsew')
square_root_btn = Button(calc, text='SQRT', command=lambda: operator_click('sqrt'), bg='#99FFFF')
square_root_btn.grid(row=1, column=4, sticky='nsew')
# Row 2
seven_btn = Button(calc, text='7', command=lambda: number_button_click(7), bg='#D3D3D3')
seven_btn.grid(row=2, column=0, sticky='nsew')
eight_btn = Button(calc, text='8', command=lambda: number_button_click(8), bg='#D3D3D3')
eight_btn.grid(row=2, column=1, sticky='nsew')
nine_btn = Button(calc, text='9', command=lambda: number_button_click(9), bg='#D3D3D3')
nine_btn.grid(row=2, column=2, sticky='nsew')
divide_btn = Button(calc, text='/', command=lambda: operator_click('divide'), bg='#99FFFF')
divide_btn.grid(row=2, column=3, sticky='nsew')
modulus_btn = Button(calc, text='%', command=lambda: operator_click('modulus'), bg='#99FFFF')
modulus_btn.grid(row=2, column=4, sticky='nsew')
# Row 3
four_btn = Button(calc, text='4', command=lambda: number_button_click(4), bg='#D3D3D3')
four_btn.grid(row=3, column=0, sticky='nsew')
five_btn = Button(calc, text='5', command=lambda: number_button_click(5), bg='#D3D3D3')
five_btn.grid(row=3, column=1, sticky='nsew')
six_btn = Button(calc, text='6', command=lambda: number_button_click(6), bg='#D3D3D3')
six_btn.grid(row=3, column=2, sticky='nsew')
multiply_btn = Button(calc, text='*', command=lambda: operator_click('multiply'), bg='#99FFFF')
multiply_btn.grid(row=3, column=3, sticky='nsew')
reciprocal_btn = Button(calc, text='1/x', command=lambda: operator_click('reciprocal'), bg='#99FFFF')
reciprocal_btn.grid(row=3, column=4, sticky='nsew')
# Row 4
one_btn = Button(calc, text='1', command=lambda: number_button_click(1), bg='#D3D3D3')
one_btn.grid(row=4, column=0, sticky='nsew')
two_btn = Button(calc, text='2', command=lambda: number_button_click(2), bg='#D3D3D3')
two_btn.grid(row=4, column=1, sticky='nsew')
three_btn = Button(calc, text='3', command=lambda: number_button_click(3), bg='#D3D3D3')
three_btn.grid(row=4, column=2, sticky='nsew')
subtract_btn = Button(calc, text='-', command=lambda: operator_click('subtract'), bg='#99FFFF')
subtract_btn.grid(row=4, column=3, sticky='nsew')
equals_btn = Button(calc, text='=', command=equals_click, bg='#99FFFF')
equals_btn.grid(row=4, column=4, rowspan=2, sticky='nsew')
# Row 5
zero_btn = Button(calc, text='0', command=lambda: number_button_click(0), bg='#D3D3D3')
zero_btn.grid(row=5, column=0, columnspan=2, sticky='nsew')
decimal_btn = Button(calc, text='.', bg='#99FFFF')
decimal_btn.grid(row=5, column=2, sticky='nsew')
add_btn = Button(calc, text='+', command=lambda: operator_click('add'), bg='#99FFFF')
add_btn.grid(row=5, column=3, sticky='nsew')


# For the program not to terminate
calc.mainloop()
