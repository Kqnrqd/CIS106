# Konrad Kolber
# 03/31/2026
# Problem 4

def input_text():
    textLine = input("Enter a line of text: ")
    return textLine


def input_chars():
    charsNum = int(input("Enter number of characters per line: "))
    return charsNum


def input_lines():
    linesNum = int(input("Enter number of lines to print: "))
    return linesNum


def input_shift():
    shiftText = input("Enter scroll direction left or right: ")
    return shiftText.lower().strip()


def build_line(textLine, charsNum):
    if len(textLine) == 0:
        return ""

    buildLine = ""

    while len(buildLine) < charsNum:
        buildLine = buildLine + textLine

    finalLine = buildLine[:charsNum]
    return finalLine


def shift_left(showLine):
    firstChar = showLine[0]
    otherText = showLine[1:]
    finalLine = otherText + firstChar
    return finalLine


def shift_right(showLine):
    lastChar = showLine[-1]
    otherText = showLine[:-1]
    finalLine = lastChar + otherText
    return finalLine


def output_scroll(showLine, linesNum, shiftText):
    countNum = 0

    while countNum < linesNum:
        print(showLine)

        if shiftText == "left":
            showLine = shift_left(showLine)
        elif shiftText == "right":
            showLine = shift_right(showLine)
        else:
            print("Invalid direction entered.")
            break

        countNum = countNum + 1


def main():
    textLine = input_text()
    charsNum = input_chars()
    linesNum = input_lines()
    shiftText = input_shift()

    showLine = build_line(textLine, charsNum)
    output_scroll(showLine, linesNum, shiftText)


main()

# Test data
# Text: Repeat this.
# Characters per line: 67
# Lines to print: 2
# Direction: left
#
# Text: Repeat this.
# Characters per line: 6
# Lines to print: 8
# Direction: right
