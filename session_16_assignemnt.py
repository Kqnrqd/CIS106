# May 7, 2026
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


class Manager(Employee):
    def long_term_bonus(self):
        return self.salary * 0.40


class Executive(Manager):
    def ExecutiveBonus(self):
        return self.salary * 2.00

    def long_term_bonus(self):
        return self.salary * 0.50


class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_sticker_price(self):
        return self.sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90


class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def set_sport_wheels(self, choice):
        self.sport_wheels = choice.upper()

    def set_sport_engine(self, choice):
        self.sport_engine = choice.upper()

    def set_sport_interior(self, choice):
        self.sport_interior = choice.upper()

    def pricewithoptions(self):
        total = self.discount_price()
        if self.sport_wheels == 'Y':
            total += 1000.00
        if self.sport_engine == 'Y':
            total += 3000.00
        if self.sport_interior == 'Y':
            total += 2000.00
        return total


class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.gps = 'N'
        self.self_driving = 'N'

    def set_gps(self, choice):
        self.gps = choice.upper()

    def set_self_driving(self, choice):
        self.self_driving = choice.upper()

    def pricewithoptions(self):
        total = self.discount_price()
        if self.gps == 'Y':
            total += 5000.00
        if self.self_driving == 'Y':
            total += 10000.00
        return total


print("--- Testing Employee Hierarchy ---")

mgr_1 = Manager('Alice', 'Smith', 80000, 0.10)
print(f"Manager: {mgr_1.fullname()}")
print(f"Long Term Bonus: ${mgr_1.long_term_bonus()}")

exec_1 = Executive('Bob', 'Johnson', 120000, 0.15)
print(f"\nExecutive: {exec_1.fullname()}")
print(f"Executive Bonus: ${exec_1.ExecutiveBonus()}")
print(f"Long Term Bonus (Overridden): ${exec_1.long_term_bonus()}")


print("\n--- Testing Car Hierarchy ---")

sport_car = Sport('Ford', 'Mustang', 30000)
sport_car.set_sport_wheels('Y')
sport_car.set_sport_engine('Y')
sport_car.set_sport_interior('N')
print(f"Sport Car: {sport_car.get_make()} {sport_car.get_model()}")
print(f"Base Discount Price: ${sport_car.discount_price()}")
print(f"Price with Selected Options: ${sport_car.pricewithoptions()}")

luxury_car = Luxury('Mercedes', 'S-Class', 90000)
luxury_car.set_gps('Y')
luxury_car.set_self_driving('Y')
print(f"\nLuxury Car: {luxury_car.get_make()} {luxury_car.get_model()}")
print(f"Base Discount Price: ${luxury_car.discount_price()}")
print(f"Price with Selected Options: ${luxury_car.pricewithoptions()}")
