# Konrad Kolber 04/07/2026

def displayforward(lastnameslist, examscorelist):
    countervalue = 0
    while countervalue < len(lastnameslist):
        print(lastnameslist[countervalue], examscorelist[countervalue])
        countervalue = countervalue + 1

def displayreverse(lastnameslist, examscorelist):
    countervalue = len(lastnameslist) - 1
    while countervalue >= 0:
        print(lastnameslist[countervalue], examscorelist[countervalue])
        countervalue = countervalue - 1

lastnamearray = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
examscorearray = [88, 92, 76, 85, 95, 81, 79, 90, 87, 93]

print("Names and scores in order")
displayforward(lastnamearray, examscorearray)

print()

print("Names and scores in reverse order")
displayreverse(lastnamearray, examscorearray)
