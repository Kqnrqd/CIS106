# Konrad Kolber
# 03/31/2026
# Problem 2

def input_text():
    textLine = input("Enter a line of text: ")
    return textLine


def clean_spaces(textLine):
    stripLine = textLine.strip()
    wordList = stripLine.split()
    cleanLine = " ".join(wordList)
    return cleanLine


def reverse_text(cleanLine):
    backLine = cleanLine[::-1]
    return backLine


def output_text(cleanLine, backLine):
    print("Cleaned text:", cleanLine)
    print("Backwards text:", backLine)


def main():
    textLine = input_text()
    cleanLine = clean_spaces(textLine)
    backLine = reverse_text(cleanLine)
    output_text(cleanLine, backLine)


main()

# Test data
#      the   cat   in   the   hat
# hello     world
#   Python
