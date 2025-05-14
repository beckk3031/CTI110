# Kyle Beck
# 09 APR 2025
# P2LAB1
# This program calculates circle formulas

radius = float(input('What is the radius of the circle? '))
pi = 3.14159

diameter = 2 * radius
circ = 2 * pi * radius
area = pi * radius ** 2

print(f'\nThe diamter of the circle is {diameter:.1f}')

print(f'\nThe circumference of the circle is {circ:.2f}')

print(f'\nThe area of the circle is {area:.3f}')
