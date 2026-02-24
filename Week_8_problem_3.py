# Konrad Kolber
# 2/23/2026

def calculatempg(milestraveledvalue, gallonsusedvalue):
    if gallonsusedvalue == 0:
        return 0
    mpgvalue = milestraveledvalue / gallonsusedvalue
    return mpgvalue

tripcountvalue = 0

userchoicevalue = input("Do program? Yes or No: ")

while userchoicevalue == "Yes":
    destinationcityvalue = input("Enter destination city: ")
    milestraveledvalue = float(input("Enter miles traveled: "))
    gallonsusedvalue = float(input("Enter gallons used: "))

    mpgvalue = calculatempg(milestraveledvalue, gallonsusedvalue)

    print("City:", destinationcityvalue)
    print("Miles:", milestraveledvalue)
    print("MPG:", mpgvalue)

    tripcountvalue = tripcountvalue + 1

    userchoicevalue = input("Do program? Yes or No: ")

print("Number of trips:", tripcountvalue)

