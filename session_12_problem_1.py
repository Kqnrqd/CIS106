# Konrad Kolber 04/07/2026

def displayforward(lastnameslist):
    countervalue = 0
    while countervalue < len(lastnameslist):
        print(lastnameslist[countervalue])
        countervalue = countervalue + 1

def displayreverse(lastnameslist):
    countervalue = len(lastnameslist) - 1
    while countervalue >= 0:
        print(lastnameslist[countervalue])
        countervalue = countervalue - 1

lastnamearray = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

print("Names in order")
displayforward(lastnamearray)

print()

print("Names in reverse order")
displayreverse(lastnamearray)
