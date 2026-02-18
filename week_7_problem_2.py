# Konrad Kolber 02/18/2026
# CIS 106 Session 7 Problem 2

first_number = 1
second_number = 1

print(first_number)
print(second_number)

for count_value in range(18):
    next_number = first_number + second_number
    print(next_number)

    first_number = second_number
    second_number = next_number

