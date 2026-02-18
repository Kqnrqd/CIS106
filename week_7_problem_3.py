# Konrad Kolber 02/18/2026
# CIS 106 Session 7 Problem 3

file_handle = open("employees.txt", "r")

total_bonus = 0.0

while True:
    last_name = file_handle.readline().strip()

    if last_name == "":
        break

    salary_value = float(file_handle.readline().strip())

    if salary_value >= 100000:
        bonus_rate = 0.20
    elif salary_value >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus_value = salary_value * bonus_rate
    total_bonus = total_bonus + bonus_value

    print(last_name, salary_value, bonus_value)

file_handle.close()

print("Total bonuses:", total_bonus)

