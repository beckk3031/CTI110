# Kyle Beck
# P3HW1
# 22 APR 2025
# This program takes a number grade, determine average
# and display a letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [
    mod_1,
    mod_2,
    mod_3,
    mod_4,
    mod_5,
    mod_6
    ]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

print('\n----------Results----------')
print(f'Lowest Grade:   {low:.1f}')
print(f'Highest Grade:  {high:.1f}')
print(f'Sum of Grades:  {total:.1f}')
print(f'Average:        {avg:.2f}')
print('-----------------------------')

# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





