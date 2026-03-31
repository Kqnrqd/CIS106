# Konrad Kolber
# 03/31/2026
# Problem 1

def input_name():
    nameLine = input("Enter a first name and last name: ")
    return nameLine


def parse_name(nameLine):
    cleanLine = nameLine.strip()
    partList = cleanLine.split()

    if len(partList) != 2:
        return False, ""

    firstName = partList[0]
    lastName = partList[1]
    firstInit = firstName[0].upper()
    finalText = lastName + ", " + firstInit + "."

    return True, finalText


def output_name(validName, finalText):
    if validName == True:
        print(finalText)
    else:
        print("Invalid input. Please enter only a first name and last name.")


def main():
    nameLine = input_name()
    validName, finalText = parse_name(nameLine)
    output_name(validName, finalText)


main()

# Test data
# John Smith
#   John Smith
# John
# John Michael Smitho
