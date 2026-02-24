# Konrad Kolber
# 2/23/2026

def calculateaverage(hitstotalvalue, atbatstotalvalue):
    if atbatstotalvalue == 0:
        return 0
    battingaveragevalue = hitstotalvalue / atbatstotalvalue
    return battingaveragevalue

playercountvalue = 0

userchoicevalue = input("Do program? Yes or No: ")

while userchoicevalue == "Yes":
    lastnamevalue = input("Enter last name: ")
    hitstotalvalue = int(input("Enter hits: "))
    atbatstotalvalue = int(input("Enter at bats: "))

    battingaveragevalue = calculateaverage(hitstotalvalue, atbatstotalvalue)

    print("Last Name:", lastnamevalue)
    print("Batting Average:", battingaveragevalue)

    playercountvalue = playercountvalue + 1

    userchoicevalue = input("Do program? Yes or No: ")

print("Number of players:", playercountvalue)
