# Kyle Beck
# 09 APR 2025
# P2HW1
# Travel expenses calculator

print('This program calculates and displays travel expense\n')

budget = int(input('Enter Budget: '))

travel_dest = input('\nEnter your travel destination: ')

gas = int(input('\nHow much do you think you will spend on gas? '))

lodging = int(input('\nApproximately, how much will you need for accomodation/hotel? '))

food = int(input('\nLast, how much do you need for food? '))

balance = budget - gas - lodging - food

print('\n------------Travel Expenses------------')

# the long space in the print statement is to ensure the city is printed on line with the numbers
print('Location:', '         ', travel_dest)

print(f'Initial Budget:     ${budget:.2f}')

print(f'Fuel:               ${gas:.2f}')

print(f'Accomodation:       ${lodging:.2f}')

print(f'Food:               ${food:.2f}')

print('----------------------------------------')

print(f'\nRemaining Balance:  ${balance:.2f}')
