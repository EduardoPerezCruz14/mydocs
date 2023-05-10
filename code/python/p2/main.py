#!/usr/bin/python3

def hello():
    return int(input('\nDesea teclear otra vez?\n1- Si\n2- No\n> '))

flag = False
option = 0

while not flag:

    dec_value = int(input('\nValor en base decimal\n> '), 10)
    
    try:
        option = int(input('\nEliga una opcion\n1- Binario\n2- Octal\n3- Hexadecimal\n4- BCD\n5- Salir\n> '), 10)
    except ValueError:
        print('\nERROR\nFavor de teclar un valor entero\n')
        break
    
    if option == 1:
        out = ''
        divi = dec_value
        
        while divi >= 1:
            
            if divi % 2 != 0:
                out = out + '1'
            else:
                out = out + '0'

            divi = int(divi/2)
        
        out = out [::-1]

        print(f'\nValor binario: {out}')
        
        if hello() == 2:
            flag = True

    elif option == 2:
        
        out = ''
        coci = dec_value

        while coci != 0:
            coci_bef = coci

            coci = int(coci / 8)
            coci_aft = coci * 8
            res = coci_bef - coci_aft

            out = out + str(res)

        out = out [::-1]

        print(f'\nValor octadecimal: {out}')

        if hello() == 2:
            flag = True

    elif option == 3:
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
        print (f"\nValor hexadecimal: {out}")

        if hello() == 2:
            flag = True

    elif option == 4:

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

        print(f'\nValor BCD: {output}')
        
        if hello() == 2:
            flag = True

    else:
        flag = True

print('\nNos vemos :)\n')