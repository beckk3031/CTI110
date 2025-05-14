# Kyle Beck
# 22 APR 2025
# P3HW2 Salary
# This program calculates slaray amount with rates and hours.

# This first portion gets data from the employee.

name = input("Enter employee's name: ")
hours = float(input('Enter number of hours worked: '))
rate = float(input("Enter employee's pay rate: "))
print('--------------------------------')

if hours > 40:
    reghour_pay = 40 * rate
else:
    reghour_pay = hours * rate

# This portion determines if the employee worked overtime.

if hours > 40:
    overtime = hours - 40
    overtime_pay = overtime * (rate * 1.5)
else:
    overtime = 0
    overtime_pay = 0

gross_pay = overtime_pay + reghour_pay

# This portion prints calculation for the employee.
# Spaces are added to print statement to senure clean output.

print('Employee name', name)

print('Hours Worked', '   ', 'Pay Rate', '   ', 'OverTime', '   ', 'OverTime Pay', '   ' 'RegHour Pay', '   ', 'Gross Pay')
print('------------------------------------------------------------------------------------------')
print('   ', hours, '         ', rate, '       ', overtime, '        ', overtime_pay, '        ', reghour_pay, '        ', gross_pay)
