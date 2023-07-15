student = dict()
student['Name'] = str(input('Name: '))
student['Average'] = float(input(f'Average grade of {student["Name"]}: '))
if student['Average'] >= 7:
    student['Situation'] = 'Approved'
elif student['Average'] < 7:
    student['Situation'] = 'Disapproved'

for k, v in student.items():
    if student['Average'] >= 7:
        print(f'\033[1m{k}\033[m = \033[1;32m{v}\033[m')
    elif student['Average'] < 7:
        print(f'\033[1m{k}\033[m = \033[1;31m{v}\033[m')