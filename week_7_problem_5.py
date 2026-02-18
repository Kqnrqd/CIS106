# Konrad Kolber 02/18/2026
# CIS 106 Session 7 Problem 5

file_handle = open("students.txt", "r")

total_tuition = 0.0
student_count = 0

while True:
    last_name = file_handle.readline().strip()

    if last_name == "":
        break

    district_code = file_handle.readline().strip()
    credits_taken = int(file_handle.readline().strip())

    if district_code == "I":
        cost_credit = 250
    else:
        cost_credit = 500

    tuition_owed = credits_taken * cost_credit

    total_tuition = total_tuition + tuition_owed
    student_count = student_count + 1

    print(last_name, credits_taken, tuition_owed)

file_handle.close()

print("Total tuition:", total_tuition)
print("Students:", student_count)

