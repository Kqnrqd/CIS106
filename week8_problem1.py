# Konrad Kolber
# 2/23/2026

def calculatetotal(quantityvalue, pricevalue):
    totalamount = quantityvalue * pricevalue
    if totalamount > 10000:
        totalamount = totalamount * 0.90
    return totalamount

extendedtotal = 0

userchoicevalue = input("Do program? Yes or No: ")

while userchoicevalue == "Yes":
    quantityvalue = float(input("Enter quantity: "))
    pricevalue = float(input("Enter price: "))

    totalamount = calculatetotal(quantityvalue, pricevalue)

    print("Quantity:", quantityvalue)
    print("Price:", pricevalue)
    print("Total:", totalamount)

    extendedtotal = extendedtotal + totalamount

    userchoicevalue = input("Do program? Yes or No: ")

print("Extended price sum:", extendedtotal)
