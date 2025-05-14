# Kyle Beck
# P4HW2
# 30 APR 2025
# Tis program computes salaries.

keep_enter = 'yes'

while keep_enter == 'yes':
    name = input("Enter employee's name or Done to terminate: ")
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
# Spaces are added to print statement to ensure clean output.

    print('Employee name', name)

    print('Hours Worked', '   ', 'Pay Rate', '   ', 'OverTime', '   ', 'OverTime Pay', '   ' 'RegHour Pay', '   ', 'Gross Pay')
    print('------------------------------------------------------------------------------------------')
    print('   ', hours, '         ', rate, '       ', overtime, '        ', overtime_pay, '        ', reghour_pay, '        ', gross_pay)

