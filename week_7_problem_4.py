# Konrad Kolber 02/18/2026
# CIS 106 Session 7 Problem 4

file_handle = open("orders.txt", "r")

total_extended = 0.0
order_count = 0

while True:
    item_name = file_handle.readline().strip()

    if item_name == "":
        break

    quantity_value = int(file_handle.readline().strip())
    price_value = float(file_handle.readline().strip())

    extended_price = quantity_value * price_value

    total_extended = total_extended + extended_price
    order_count = order_count + 1

    print(item_name, quantity_value, price_value, extended_price)

file_handle.close()

average_order = total_extended / order_count

print("Total:", total_extended)
print("Orders:", order_count)
print("Average:", average_order)
