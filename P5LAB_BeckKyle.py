# Kyle Beck
# P5LAB
# 06 MAY 2025
# This program calculates change owed to a customer.

import random

money = round(random.uniform(0.01, 100.00), 2)

def print_disperse_change():
    cents = (money - paid) * 100

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents
    if money == 0:
        print('No change')
    if dollars > 0:
        if dollars == 1:
            print(f'{dollars:.0f}', 'Dollar')
        else:
            print(f'{dollars:.0f}', 'Dollars')
    if quarters > 0:
        if quarters == 1:
            print(f'{quarters:.0f}', 'Quarter')
        else:
            print(f'{quarters:.0f}', 'Quarters')
    if dimes > 0:
        if dimes == 1:
            print(f'{dimes:.0f}', 'Dime')
        else:
            print(f'{dimes:.0f}', 'Dimes')
    if nickels > 0:
        if nickels == 1:
            print(f'{nickels:.0f}', 'Nickel')
        else:
            print(f'{nickels:.0f}', 'Nickels')
    if pennies > 0:
        if pennies == 1:
            print(f'{pennies:.0f}', 'Penny')
        else:
            print(f'{pennies:.0f}', 'Pennies')
print(f'You owe ${money}')
paid = float(input('How much cash will you put in the self-checkout? '))
change = paid - money
print(f'Change is: ${change:.2f}')
print_disperse_change()
