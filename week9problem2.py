# Konrad Kolber
# 03/03/2026

def roomSquareFeet(roomLength, roomWidth, roomHeight):

    squareFeet = (2 * roomLength * roomWidth) + (2 * roomLength * roomHeight) + (2 * roomWidth * roomHeight)

    return squareFeet


userAnswer = input("Do you want to run program Yes or No ")

while userAnswer == "Yes":

    roomLength = float(input("Enter length "))
    roomWidth = float(input("Enter width "))
    roomHeight = float(input("Enter height "))

    squareFeet = roomSquareFeet(roomLength, roomWidth, roomHeight)

    gallonsNeeded = squareFeet / 50

    print("Gallons needed", gallonsNeeded)

    userAnswer = input("Do you want to continue Yes or No ")
