#!/usr/bin/python3

import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

flag = True

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x240")
app.title('Numeric Systems')

def button_function():
    try: 
        dec_value = int(entry.get())
    except:
        flag = False

# Using CTkLabel
label = customtkinter.CTkLabel(app, text="Valor decimal")
label.place(relx=0.05, rely=0.08)

# Use CTkButton
button = customtkinter.CTkButton(master=app, text="Process", command=button_function)
button.place(relx=0.165, rely=0.4, anchor=tk.CENTER)

# Use CTkEntry 
entry = customtkinter.CTkEntry(app, placeholder_text="Base 10")
entry.place(relx=0.05, rely=0.2)

octalVal = customtkinter.CTkLabel(app, text="Valor octal:")
octalVal.place(relx=0.6, rely=0.1)

hexVal = customtkinter.CTkLabel(app, text="Valor hexadecimal:")
hexVal.place(relx=0.525, rely=0.25)

binVal = customtkinter.CTkLabel(app, text="Valor binario:")
binVal.place(relx=0.5825, rely=0.4)

bcdVal = customtkinter.CTkLabel(app, text="Valor BCD:")
bcdVal.place(relx=0.6, rely=0.55)

app.mainloop()