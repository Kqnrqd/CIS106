# Konrad Kolber 04/07/2026

def displayplayers(playernamearray, battingarray):
    countervalue = 0
    while countervalue < len(playernamearray):
        print(playernamearray[countervalue], battingarray[countervalue])
        countervalue = countervalue + 1

def searchplayer(playernamearray, battingarray, searchvalue):
    countervalue = 0
    while countervalue < len(playernamearray):
        if playernamearray[countervalue].lower() == searchvalue.lower():
            print("Player found")
            print(playernamearray[countervalue], battingarray[countervalue])
            return
        countervalue = countervalue + 1

playernamearray = []
battingavgarray = []

inputfilehandle = open("players.txt", "r")

for filelinevalue in inputfilehandle:
    datavalues = filelinevalue.strip().split()
    playernamearray.append(datavalues[0])
    battingavgarray.append(float(datavalues[1]))

inputfilehandle.close()

displayplayers(playernamearray, battingavgarray)

searchagainvalue = "yes"

while searchagainvalue.lower() == "yes":
    lastnamevalue = input("Enter a last name to search for: ")
    searchplayer(playernamearray, battingavgarray, lastnamevalue)
    searchagainvalue = input("Do you want to search again? ")
