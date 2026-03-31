# Konrad Kolber
# 03/31/2026
# Problem 3

def input_csv():
    valueLine = input("Enter comma separated values: ")
    return valueLine


def parse_csv(valueLine):
    splitList = valueLine.split(",")
    cleanList = []

    for itemValue in splitList:
        cleanItem = itemValue.strip()
        cleanList.append(cleanItem)

    return cleanList


def output_csv(cleanList):
    print("Items:")
    for itemValue in cleanList:
        print(itemValue)


def main():
    valueLine = input_csv()
    cleanList = parse_csv(valueLine)
    output_csv(cleanList)


main()

# Test data
# 67, 41, 10, clock
# globe, cake, carseat
# John Smith, Banana Grape, David Adam
