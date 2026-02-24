# Konrad Kolber
# 2/23/2026

def getpayratevalue(jobcodevalue):
    if jobcodevalue == "L":
        return 25
    elif jobcodevalue == "A":
        return 30
    elif jobcodevalue == "J":
        return 50
    else:
        return 0

totalgrosspayvalue = 0

userchoicevalue = input("Do program? Yes or No: ")

while userchoicevalue == "Yes":
    employeelastnamevalue = input("Enter last name: ")
    jobcodevalue = input("Enter job code: ")
    hoursworkedvalue = float(input("Enter hours worked: "))

    payratevalue = getpayratevalue(jobcodevalue)

    if hoursworkedvalue <= 40:
        grosspayvalue = hoursworkedvalue * payratevalue
    else:
        overtimehoursvalue = hoursworkedvalue - 40
        grosspayvalue = (40 * payratevalue) + (overtimehoursvalue * payratevalue * 1.5)

    print("Last Name:", employeelastnamevalue)
    print("Gross Pay:", grosspayvalue)

    totalgrosspayvalue = totalgrosspayvalue + grosspayvalue

    userchoicevalue = input("Do program? Yes or No: ")

print("Total Gross Pay:", totalgrosspayvalue)
