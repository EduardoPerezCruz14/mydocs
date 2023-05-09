#!/usr/bin/python3

flag_op = False
flag = False

while not flag_op:
    base_number = 0

    option = int(input('\nSelect which base number do you have:\n1- Decimal\n2- Binary\n3- Hexadecimal\n4- Exit\n> '))

    if option == 1:
        text_value = 'decimal'
        base_number = 10
    elif option == 2:
        text_value = 'binary'
        base_number = 2
    elif option == 3:
        text_value = 'hexadecimal'
        base_number = 16
    elif option > 3:
        flag_op = True

    if not flag_op:
        flag_op = True
        try:
            binary_value = int(input(f'\nEnter a {text_value} number\n> '), base=base_number) 
            print()
        except:
            print(f'You cannot insert another base format, you can only type as a {text_value} number')
            flag = True

if not flag and option < 4:
    print(f'Binary number:\t\t{binary_value :b}\nDecimal number:\t\t{binary_value}\nHexadecimal number:\t{binary_value :X}')