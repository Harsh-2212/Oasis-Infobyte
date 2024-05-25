#Importing Necessary Dependencies
from tkinter import *
from tkinter import messagebox
import random

#Creating frame
root = Tk()
root.title('Strong - Password Generator')
root.geometry('500x400')

#logic to generate random password from string, integer and character provided by user
def generate_password():
    pw_entry.delete(0, END)
    
    input_string = string_entry.get()
    numbers = num_entry.get()
    symbols = special_entry.get()
    
    try:
        pw_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the password length")
        return
    
    combined_string = input_string + numbers + symbols
    
    if pw_length > len(combined_string):
        messagebox.showerror("Error", "Password length cannot be greater than the combined length of the input string, numbers, and symbols")
        return

    my_password = ''.join(random.sample(combined_string, pw_length))

    pw_entry.insert(0, my_password)

#Clipboard Copy logic
def clipper():
    
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

#front-end logic for taking user input
lf_string = LabelFrame(root, text='Input String')
lf_string.pack(pady=10)

string_entry = Entry(lf_string, width=40)
string_entry.pack(padx=10, pady=5)

lf_numbers = LabelFrame(root, text='Numbers')
lf_numbers.pack(pady=10)

num_entry = Entry(lf_numbers, width=40)
num_entry.pack(padx=10, pady=5)

lf_symbols = LabelFrame(root, text='Symbols')
lf_symbols.pack(pady=10)

special_entry = Entry(lf_symbols, width=40)
special_entry.pack(padx=10, pady=5)

lf_length = LabelFrame(root, text='Password Length')
lf_length.pack(pady=10)

length_entry = Entry(lf_length, width=40)
length_entry.pack(padx=10, pady=5)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text='Generate Random Password', command=generate_password)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

#viewing the random generated password
pw_entry = Entry(root, text='', font=('Helvetica', 16), width=40)
pw_entry.pack(pady=10)

root.mainloop()

#Implementation
#python main.py