# Konrad Kolber 02/18/2026
# CIS 106 Session 7 Problem 1

continue_value = "Y"

while continue_value == "Y":
    principal_amount = float(input("Enter principle amount: "))
    interest_rate = float(input("Enter interest rate: "))

    beginning_balance = principal_amount
    total_interest = 0.0

    print("Year Beginning Ending")

    for year_number in range(1, 6):
        interest_value = beginning_balance * interest_rate
        ending_balance = beginning_balance + interest_value
        total_interest = total_interest + interest_value

        print(year_number, format(beginning_balance, ",.2f"), format(ending_balance, ",.2f"))

        beginning_balance = ending_balance

    print("Total interest earned:", format(total_interest, ",.2f"))

    continue_value = input("Run again Y or N: ").upper()
