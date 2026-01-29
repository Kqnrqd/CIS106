# Date: 1/26/2026 Konrad Kolber

print("Program 1")

quantityAmountValue = float(input("Enter the quantity: "))

if quantityAmountValue >= 1000:
    unitPriceValue = 3.00
else:
    unitPriceValue = 5.00

extendedPriceValue = quantityAmountValue * unitPriceValue
taxAmountValue = extendedPriceValue * 0.07
totalPriceValue = extendedPriceValue + taxAmountValue

print("Quantity:", quantityAmountValue)
print("Unit Price:", unitPriceValue)
print("Extended Price:", extendedPriceValue)
print("Tax:", taxAmountValue)
print("Total:", totalPriceValue)

print("")

print("Program 2")

itemLetterValue = input("Enter item letter: ")
quantityAmountValue = float(input("Enter quantity: "))

if itemLetterValue == "A":
    unitPriceAmountValue = 10.00
else:
    unitPriceAmountValue = 20.00

extendedPriceAmountValue = quantityAmountValue * unitPriceAmountValue

print("Item:", itemLetterValue)
print("Unit Price:", unitPriceAmountValue)
print("Extended Price:", extendedPriceAmountValue)

print("")

print("Program 3")

numberOfBooksValue = float(input("Enter number of books: "))
costPerBookValue = float(input("Enter cost per book: "))

orderTotalValue = numberOfBooksValue * costPerBookValue

if orderTotalValue > 50.00:
    shippingChargeValue = 0
else:
    shippingChargeValue = 25.00

print("Order Total:", orderTotalValue)
print("Shipping Charge:", shippingChargeValue)

print("")

print("Program 4")

applianceNameValue = input("Enter appliance name: ")
applianceCostValue = float(input("Enter appliance cost: "))

if applianceCostValue > 1000.00:
    warrantyCostValue = applianceCostValue * 0.10
else:
    warrantyCostValue = applianceCostValue * 0.05

totalCostValue = applianceCostValue + warrantyCostValue

print("Appliance Name:", applianceNameValue)
print("Appliance Cost:", applianceCostValue)
print("Warranty Cost:", warrantyCostValue)
print("Total Cost:", totalCostValue)

print("")

print("Program 5")

lastNameValue = input("Enter last name: ")
dependentCountValue = float(input("Enter number of dependents: "))
grossIncomeValue = float(input("Enter gross income: "))

adjustedIncomeValue = grossIncomeValue - (dependentCountValue * 12000)

if adjustedIncomeValue > 50000:
    taxRateValue = 0.20
else:
    taxRateValue = 0.10

incomeTaxValue = adjustedIncomeValue * taxRateValue

if incomeTaxValue < 0:
    incomeTaxValue = 100

print("Last Name:", lastNameValue)
print("Gross Income:", grossIncomeValue)
print("Number of Dependents:", dependentCountValue)
print("Adjusted Gross Income:", adjustedIncomeValue)
print("Income Tax:", incomeTaxValue)

