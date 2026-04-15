# Konrad Kolber 4/13/26

numberitems = int(input("Enter how many numbers: "))

firstlist = []

for countervalue in range(numberitems):
    usernumber = int(input("Enter a number: "))
    firstlist.append(usernumber)

print(firstlist)

firstlist.insert(1, 99)
print(firstlist)

indexvalue = firstlist.index(99)
firstlist[indexvalue] = 100
print(firstlist)

secondlist = [500, 600, 700, 800, 900]
print(secondlist)

firstlist.extend(secondlist)
print(firstlist)

firstlist.remove(800)
print(firstlist)

del firstlist[2]
print(firstlist)

gradeslist = ["A", "B", "C", "A", "A", "C"]

countvalue = gradeslist.count("A")
print(countvalue)

indexb = gradeslist.index("B")
print(indexb)

if "F" in gradeslist:
    print("F is in the list")
else:
    print("F is not in the list")

secondlist.clear()
print(secondlist)

del secondlist

try:
    print(secondlist)
except:
    print("secondlist does not exist")

playerslist = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
playerslist.sort()
print(playerslist)

playerscopy = playerslist.copy()
print(playerscopy)

playerscopy.reverse()
print(playerslist)
print(playerscopy)
