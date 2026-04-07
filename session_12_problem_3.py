# Konrad Kolber 04/07/2026

def displayrecords(lastnameslist, examscorelist):
    countervalue = 0
    while countervalue < len(lastnameslist):
        print(lastnameslist[countervalue], examscorelist[countervalue])
        countervalue = countervalue + 1

def highestscore(lastnameslist, examscorelist):
    highvalue = 0
    highindexvalue = 0
    countervalue = 0

    while countervalue < len(examscorelist):
        if examscorelist[countervalue] > highvalue:
            highvalue = examscorelist[countervalue]
            highindexvalue = countervalue
        countervalue = countervalue + 1

    print("Highest score")
    print(lastnameslist[highindexvalue], highvalue)

def lowestscore(lastnameslist, examscorelist):
    lowvaluevalue = 999
    lowindexvalue = 0
    countervalue = 0

    while countervalue < len(examscorelist):
        if examscorelist[countervalue] < lowvaluevalue:
            lowvaluevalue = examscorelist[countervalue]
            lowindexvalue = countervalue
        countervalue = countervalue + 1

    print("Lowest score")
    print(lastnameslist[lowindexvalue], lowvaluevalue)

lastnamearray = []
examscorearray = []

inputfilehandle = open("scores.txt", "r")

for filelinevalue in inputfilehandle:
    datavalues = filelinevalue.strip().split()
    lastnamearray.append(datavalues[0])
    examscorearray.append(int(datavalues[1]))

inputfilehandle.close()

displayrecords(lastnamearray, examscorearray)
print()
highestscore(lastnamearray, examscorearray)
print()
lowestscore(lastnamearray, examscorearray)
