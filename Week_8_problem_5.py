# Konrad Kolber
# 2/23/2026

def calculatetuitionvalue(credithoursvalue, districtcodevalue):
    if districtcodevalue == "I":
        tuitionowedvalue = credithoursvalue * 250
    elif districtcodevalue == "O":
        tuitionowedvalue = credithoursvalue * 550
    else:
        tuitionowedvalue = 0
    return tuitionowedvalue

totaltuitionvalue = 0

userchoicevalue = input("Do program? Yes or No: ")

while userchoicevalue == "Yes":
    studentlastnamevalue = input("Enter student last name: ")
    credithoursvalue = int(input("Enter credit hours: "))
    districtcodevalue = input("Enter district code: ")

    tuitionowedvalue = calculatetuitionvalue(credithoursvalue, districtcodevalue)

    print("Student:", studentlastnamevalue)
    print("Tuition Owed:", tuitionowedvalue)

    totaltuitionvalue = totaltuitionvalue + tuitionowedvalue

    userchoicevalue = input("Do program? Yes or No: ")

print("Total Tuition:", totaltuitionvalue)
