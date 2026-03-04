# Konrad Kolber
# 03/03/2026

def ticketPrice(milesDistance):

    if milesDistance >= 30:
        ticketCost = 12
    elif milesDistance >= 20:
        ticketCost = 10
    elif milesDistance >= 10:
        ticketCost = 8
    else:
        ticketCost = 5

    return ticketCost


totalTicketValue = 0

userAnswer = input("Do you want to run program Yes or No ")

while userAnswer == "Yes":

    lastNameInput = input("Enter last name ")
    milesDistance = int(input("Enter miles from Chicago "))

    ticketCost = ticketPrice(milesDistance)

    totalTicketValue = totalTicketValue + ticketCost

    print("Ticket price", ticketCost)

    userAnswer = input("Do you want to continue Yes or No ")

print("Total ticket price", totalTicketValue)
