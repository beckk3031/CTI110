# Kyle Beck
# 01 APR 2025
# P1HW2
# This program is meant to perform simple calculations for travel planning and expenses.

# \n is placed throughtout the program to add intential blank lines in the program.
# This is so the program outputs are neatly organized for the user.

print('This program calculates and displays travel expense\n')

budget = int(input('Enter Budget: '))

travel_dest = input('\nEnter your travel destination: ')

gas = int(input('\nHow much do you think you will spend on gas? '))

lodging = int(input('\nApproximately, how much will you need for accomodation/hotel? '))

food = int(input('\nLast, how much do you need for food? '))

print('------------Travel Expenses------------')
# I left each line as an individual print statement for ease of use and updating the program.

print('Location:', travel_dest)

print('Initial Budget:', budget)

print('\nFuel:', gas)

print('Accomodation:', lodging)

print('Food:', food)

print('\nRemaining Balance:', budget - gas - lodging - food)
