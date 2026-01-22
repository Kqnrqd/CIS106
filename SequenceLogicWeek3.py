# Date Created: 01/07/2026 Name: Konrad Kolber

print("Problem 1")

stocktickername = input("Enter stock ticker symbol: ")
numbersharesowned = float(input("Enter number of shares: "))
costpershareprice = float(input("Enter cost per share: "))

totalamountinvested = numbersharesowned * costpershareprice

print("Amount invested:", totalamountinvested)


print("Problem 2")

studentlastname = input("Enter student last name: ")
midtermexamgrade = float(input("Enter midterm exam score: "))
finalexamgrade = float(input("Enter final exam score: "))

totalexampoints = midtermexamgrade + finalexamgrade

print("Student last name:", studentlastname)
print("Total exam points:", totalexampoints)


print("Problem 3")

totaljobpayment = float(input("Enter total amount received: "))

paymentperperson = totaljobpayment / 3

print("Each person receives:", paymentperperson)


print("Problem 4")

automakename = input("Enter auto make: ")
automodelname = input("Enter auto model: ")
automsrpamount = float(input("Enter MSRP amount: "))
discountpercentage = float(input("Enter discount percent as a decimal: "))

discountamountoff = automsrpamount * discountpercentage
discountedpriceamount = automsrpamount - discountamountoff

print("Auto make:", automakename)
print("Auto model:", automodelname)
print("MSRP:", automsrpamount)
print("Discount percent:", discountpercentage)
print("Amount off:", discountamountoff)
print("Discounted price:", discountedpriceamount)


print("Problem 5")

circlepiratio = 3.174
circleradiusvalue = float(input("Enter radius of the circle: "))

circlearearesult = circlepiratio * (circleradiusvalue * circleradiusvalue)
circleperimeterresult = 2 * circlepiratio * circleradiusvalue

print("Circle area:", circlearearesult)
print("Circle perimeter:", circleperimeterresult)

