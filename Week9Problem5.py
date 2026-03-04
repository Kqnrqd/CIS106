# Konrad Kolber
# 03/03/2026

def assessedValue(countyName, marketValue):

    if countyName == "Cook":
        percentValue = 0.90
    elif countyName == "DuPage":
        percentValue = 0.80
    elif countyName == "McHenry":
        percentValue = 0.75
    elif countyName == "Kane":
        percentValue = 0.60
    else:
        percentValue = 0.70

    assessedAmount = marketValue * percentValue

    return assessedAmount


totalMarketValue = 0
totalAssessedValue = 0

userAnswer = input("Do you want to run program Yes or No ")

while userAnswer == "Yes":

    countyName = input("Enter county ")
    marketValue = float(input("Enter market value "))

    totalMarketValue = totalMarketValue + marketValue

    assessedAmount = assessedValue(countyName, marketValue)

    totalAssessedValue = totalAssessedValue + assessedAmount

    print("Assessed value", assessedAmount)

    userAnswer = input("Do you want to continue Yes or No ")

print("Total market value", totalMarketValue)
print("Total assessed value", totalAssessedValue)

