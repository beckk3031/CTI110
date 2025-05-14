# Kyle Beck
# 09 APR 2025
# P2HW2
# Program creates a list of grades

mod_grade1 = float(input('Enter grade for Module 1: '))
mod_grade2 = float(input('Enter grade for Module 2: '))
mod_grade3 = float(input('Enter grade for Module 3: '))
mod_grade4 = float(input('Enter grade for Module 4: '))
mod_grade5 = float(input('Enter grade for Module 5: '))
mod_grade6 = float(input('Enter grade for Module 6: '))

grade_list = [
    mod_grade1,
    mod_grade2,
    mod_grade3,
    mod_grade4,
    mod_grade5,
    mod_grade6,
    ]

print('\n----------Results----------')
min_grade = min(grade_list)
max_grade = max(grade_list)
sum_grade = sum(grade_list)
average = sum(grade_list) / len(grade_list)
print(f'Lowest Grade:   {min_grade:.1f}')
print(f'Highest Grade:  {max_grade:.1f}')
print(f'Sum of Grades:  {sum_grade:.1f}')
print(f'Average:        {average:.2f}')
print('----------------------------')
