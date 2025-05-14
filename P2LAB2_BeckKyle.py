# Kyle Beck
# 09 APR 2025
# P2LAB2
# This progam demonstates the usage of dictionaries

my_dict = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
    }
keys = my_dict.keys()
print(keys)
vehicle = input("\nEnter a vehicle to see it's mpg: ")
print('\nThe', vehicle, 'gets', my_dict[vehicle], 'mpg.')
distance = float(input(f'\nHow many miles will you drive the {vehicle}? '))
gallons = distance / my_dict[vehicle]
print(f'\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {distance} miles.')
