"""Employee Raise processor without Classes"""

employees = [
    {
        'first_name': 'Alice',
        'last_name': 'Atkins',
        'salary': 50000,
        'position': 'Manager',
        'years': 10
    },
    {
        'first_name': 'Bob',
        'last_name': 'Butler',
        'salary': 45000,
        'position': 'Sales Agent',
        'years': 2
    }
]

raises = [
    ('Manager', 0.1, 5),
    ('Sales Agent', 0.05, 3)
]

def apply_anniversary(employee):
    # Note the bug here.  Poor Bob!
    employee['yaers'] = employee['years'] + 1

def maybe_apply_raise(employee, raises):
    for position, amount, years in raises:
        if employee['position'] == position and employee['years'] >= years:
            raise_amount = round(employee['salary'] * amount)
            print(
                f'{employee["first_name"]} {employee["last_name"]} '
                f'gets a raise of {raise_amount}'
            )
            employee['salary'] += raise_amount
            break
    else:
        print(f'No raise for {employee["first_name"]} {employee["last_name"]}')

for employee in employees:
    apply_anniversary(employee)
    maybe_apply_raise(employee, raises)
