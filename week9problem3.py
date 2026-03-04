# Konrad Kolber
# 03/03/2026

def outDoorPrice(msrpAmount, carMake, carModel, electricCode):

    if electricCode == "Y":
        percentValue = 0.30
    elif carMake == "Honda" and carModel == "Accord":
        percentValue = 0.10
    elif carMake == "Toyota" and carModel == "Rav4":
        percentValue = 0.15
    else:
        percentValue = 0.05

    discountAmount = msrpAmount * percentValue

    newPrice = msrpAmount - discountAmount

    salesTax = newPrice * 0.07

    finalPrice = newPrice + salesTax

    return finalPrice


totalMsrpValue = 0
totalSalesValue = 0

userAnswer = input("Do you want to run program Yes or No ")

while userAnswer == "Yes":

    carMake = input("Enter make ")
    carModel = input("Enter model ")
    electricCode = input("Enter electric code Y or N ")
    msrpAmount = float(input("Enter msrp "))

    totalMsrpValue = totalMsrpValue + msrpAmount

    finalPrice = outDoorPrice(msrpAmount, carMake, carModel, electricCode)

    totalSalesValue = totalSalesValue + finalPrice

    print("Out the door price", finalPrice)

    userAnswer = input("Do you want to continue Yes or No ")

print("Total MSRP", totalMsrpValue)
print("Total Sales Price", totalSalesValue)
