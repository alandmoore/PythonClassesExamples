"""Employee Raise calculator with Classes"""

from dataclasses import dataclass


@dataclass  # New Python 3.7 feature
class Raise:
    position: str
    raise_pct: float
    years_required: int


class Employee:

    positions = ('Manager', 'Sales Agent')

    # prevent accidental addition of instance attributes:
    __slots__ = 'first', 'last', 'salary', 'position', 'years'

    def __init__(self, first, last, salary, position, years):
        self.first = first
        self.last = last
        self.salary = salary
        assert isinstance(salary, int), "Salary must be an int"
        self.position = position
        assert self.position in self.positions, "Position not valid"
        self.years = years
        assert isinstance(years, int), "Years must be an int"

    def apply_anniversary(self):
        self.years = self.years + 1

    def is_position(self, position):
        return self.position == position

    def has_worked_years(self, years):
        return self.years >= years

    def maybe_apply_raise(self, raise_obj:Raise):
        assert isinstance(raise_obj, Raise), "maybe_apply_raise requires a Raise object"
        pos = raise_obj.position
        years = raise_obj.years_required
        if self.is_position(pos) and self.has_worked_years(years):
            raise_amount = self.salary * raise_obj.raise_pct
            print(f'{self} is getting a raise of {raise_amount}')
            self.salary += raise_amount
            return True

    def __str__(self):
        return f'{self.first} {self.last}'


employees = [
    # Note that we can use positional arguments, or keywords if we want to be explicit.
    Employee('Alice', 'Atkins', 50000, 'Manager', 10),
    Employee(first='Bob', last='Butler', position='Sales Agent', salary=45000, years=2)
]

raises = [
    Raise('Manager', 0.1, 5),
    Raise(position='Sales Agent', raise_pct=0.05, years_required=3)
]

for employee in employees:
    employee.apply_anniversary()
    for r in raises:
        if employee.maybe_apply_raise(r):
            break
    else:
        print(f'No raise for {employee}.' )
