# Kyle Beck
# P3LAB
# 21 APR 2025
# This program computes the most efficient number of coins
# based on a float input.

money = float(input('Enter the amount of money as a float: '))

cents = money * 100

dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Using nested if staements to ensure plurality is corrent for number of coins.

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
