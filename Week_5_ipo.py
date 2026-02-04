# Date: 02/03/2026 Name: Konrad Kolber

print("Problem 1")

widgetQuantityValue = float(input("Enter quantity of widgets: "))

if widgetQuantityValue > 10000:
    widgetPriceValue = 10
elif widgetQuantityValue >= 5000:
    widgetPriceValue = 20
else:
    widgetPriceValue = 30

extendedPriceValue = widgetQuantityValue * widgetPriceValue
taxAmountValue = extendedPriceValue * 0.07
totalCostValue = extendedPriceValue + taxAmountValue

print("Extended Price:", extendedPriceValue)
print("Tax Amount:", taxAmountValue)
print("Total Cost:", totalCostValue)

print("")

print("Problem 2")

partNumberValue = input("Enter part number: ")
partQuantityValue = float(input("Enter quantity: "))

if partNumberValue == "10" or partNumberValue == "55":
    unitCostValue = 1.00
elif partNumberValue == "99":
    unitCostValue = 2.00
elif partNumberValue == "80" or partNumberValue == "70":
    unitCostValue = 3.00
else:
    unitCostValue = 5.00

totalPartCostValue = partQuantityValue * unitCostValue

print("Part Number:", partNumberValue)
print("Unit Cost:", unitCostValue)
print("Total Cost:", totalPartCostValue)

print("")

print("Problem 3")

principleAmountValue = float(input("Enter principle amount: "))
maturityYearsValue = float(input("Enter years to maturity: "))

if principleAmountValue > 100000 and maturityYearsValue == 5:
    interestRateValue = 0.06
elif principleAmountValue >= 50000 and principleAmountValue <= 100000 and maturityYearsValue == 10:
    interestRateValue = 0.05
elif principleAmountValue >= 50000 and principleAmountValue <= 100000 and maturityYearsValue == 5:
    interestRateValue = 0.04
else:
    interestRateValue = 0.02

firstYearInterestValue = principleAmountValue * interestRateValue

print("Principle Amount:", principleAmountValue)
print("Interest Rate:", interestRateValue)
print("First Year Interest:", firstYearInterestValue)

print("")

print("Problem 4")

ticketQuantityValue = float(input("Enter number of tickets: "))

if ticketQuantityValue >= 25:
    ticketPriceValue = 50
elif ticketQuantityValue >= 10:
    ticketPriceValue = 60
elif ticketQuantityValue >= 5:
    ticketPriceValue = 70
else:
    ticketPriceValue = 75

totalTicketCostValue = ticketQuantityValue * ticketPriceValue

print("Number of Tickets:", ticketQuantityValue)
print("Price Per Ticket:", ticketPriceValue)
print("Total Cost:", totalTicketCostValue)

print("")

print("Problem 5")

employeeLastNameValue = input("Enter employee last name: ")
employeeSalaryValue = float(input("Enter salary: "))
jobLevelValue = float(input("Enter job level: "))

if jobLevelValue >= 10:
    bonusRateValue = 0.25
elif jobLevelValue >= 5:
    bonusRateValue = 0.20
else:
    bonusRateValue = 0.10

bonusAmountValue = employeeSalaryValue * bonusRateValue

print("Employee Last Name:", employeeLastNameValue)
print("Bonus Amount:", bonusAmountValue)

