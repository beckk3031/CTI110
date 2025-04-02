# Kyle Beck
# 31 MAR 2025
# P1HW1
# This program is meant to be a calculator meant to build and refine basic coding skills

print('-----Calculating Exponents-----\n')

#when using the input variable a runtime error occured
#therefore I had to declare that the inputs are integers so they can calcualted

base = int(input('Enter an integer as the base value: '))
exponent = int(input('Enter an integer as the exponent: '))

print('\n', base, 'raised to the power of', exponent, 'is', base ** exponent, '!!')

print('\n-----Addition and Subtraction-----\n')

start_int = int(input('Enter a starting integer: '))
add_int = int(input('Enter an integer to add: '))
sub_int = int(input('Enter an integer to subtract: '))

print('\n', start_int, '+', add_int, '-', sub_int, 'is equal to', start_int + add_int - sub_int)
