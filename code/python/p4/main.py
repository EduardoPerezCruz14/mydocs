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
        flag = True
    except:
        flag = False

    if flag:

        # DECIMAL TO BIN
        out = ''
        divi = dec_value
        
        while divi >= 1:
            
            if divi % 2 != 0:
                out = out + '1'
            else:
                out = out + '0'

            divi = int(divi/2)
        
        out = out [::-1]

        binVal.configure(text=f"Valor binario: {out}")

        # DECIMAL TO OCTAL
        out = ''
        coci = dec_value

        while coci != 0:
            coci_bef = coci

            coci = int(coci / 8)
            coci_aft = coci * 8
            res = coci_bef - coci_aft

            out = out + str(res)

        out = out [::-1]

        octalVal.configure(text=f'Valor octaldecimal: {out}')

        # DECIMAL TO HEX
        out = ''
        divi = dec_value
        
        while divi >= 1:
            divi2 = int(divi/16)
            mult = divi2 * 16
            res = divi - mult
            divi = divi2

            if res == 10:
                out = out + "A"
            elif res == 11:
                out = out + "B"
            elif res == 12:
                out = out + "C"
            elif res == 13:
                out = out + "D"
            elif res == 14:
                out = out + "E"
            elif res == 15:
                out = out + "F"
            else:
                out = out + str(res)

        out = out[::-1]

        hexVal.configure(text=f"Valor hexadecimal: {out}")

        # DECIMAL TO BCD 
        dec_str = str(dec_value)
        output = ''

        for char in dec_str:
            num_char = int(char)
            
            out = ''
            divi = num_char
            
            while divi >= 1 or len(out) != 4:
                
                if divi % 2 != 0:
                    out = out + '1'
                else:
                    out = out + '0'

                divi = int(divi/2)
            
            out = out [::-1]

            output = output + out + ' '

        bcdVal.configure(text=f'Valor BCD: {output}')

xspace = 0.1

# Using CTkLabel
label = customtkinter.CTkLabel(app, text="Valor decimal")
label.place(relx=0.05, rely=0.08)

# Use CTkButton
button = customtkinter.CTkButton(master=app, text="Enviar", command=button_function)
button.place(relx=0.165, rely=0.4, anchor=tk.CENTER)

# Use CTkEntry 
entry = customtkinter.CTkEntry(app, placeholder_text="Base 10")
entry.place(relx=0.05, rely=0.2)

octalVal = customtkinter.CTkLabel(app, text="Valor octaldecimal:")
octalVal.place(relx=0.525-xspace, rely=0.1)

hexVal = customtkinter.CTkLabel(app, text="Valor hexadecimal:")
hexVal.place(relx=0.525-xspace, rely=0.25)

binVal = customtkinter.CTkLabel(app, text="Valor binario:")
binVal.place(relx=0.5825-xspace, rely=0.4)

bcdVal = customtkinter.CTkLabel(app, text="Valor BCD:")
bcdVal.place(relx=0.6-xspace, rely=0.55)

app.mainloop()