# Konrad Kolber
# 03/03/2026

def forecastSales(monthInput, salesAmount):

    if monthInput == "Jan" or monthInput == "Feb" or monthInput == "Mar":
        percentValue = 0.10
    elif monthInput == "Apr" or monthInput == "May" or monthInput == "Jun":
        percentValue = 0.15
    elif monthInput == "Jul" or monthInput == "Aug" or monthInput == "Sep":
        percentValue = 0.20
    else:
        percentValue = 0.25

    nextMonthSales = salesAmount * (1 + percentValue)

    return nextMonthSales


userAnswer = input("Do you want to run program Yes or No ")

while userAnswer == "Yes":

    lastNameInput = input("Enter last name ")
    monthInput = input("Enter month ")
    salesAmount = float(input("Enter sales "))

    forecastValue = forecastSales(monthInput, salesAmount)

    print("Next month forecast", forecastValue)

    userAnswer = input("Do you want to continue Yes or No ")
