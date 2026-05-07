# May 6, 2026
# Konrad Kolber

class Employee:
    def __init__(self, first, last, salary, bonus_rate):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@email.com'
        self.bonus_rate = bonus_rate  

    def fullname(self):
        return f"{self.first} {self.last}"

    def get_bonus_amount(self):
        return self.salary * self.bonus_rate

    def get_total_compensation(self):
        bonus_amount = self.get_bonus_amount()
        return self.salary + bonus_amount


emp_1 = Employee('Jane', 'Doe', 60000, 0.05)

print(f"Employee: {emp_1.fullname()}")
print(f"Email: {emp_1.email}")
print(f"Base Salary: ${emp_1.salary}")
print(f"Bonus Amount: ${emp_1.get_bonus_amount()}")
print(f"Total Compensation: ${emp_1.get_total_compensation()}")
