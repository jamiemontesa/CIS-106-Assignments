# Jamie M7P5.py 10/07/2026

total_discount = 0

item_order = input("Do you want to enter an item order? ")

while item_order == "yes":
    quantity = int(input("Enter the quantity: "))
    item_price = float(input("Enter the item price: $"))

    extended_price = quantity * item_price

    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total_amount = extended_price - discount_amount

    print("The extended price is: $", format(extended_price, ".2f"))
    print("The discount amount is: $", format(discount_amount, ".2f"))
    print("The total amount is: $", format(total_amount, ".2f"))

    total_discount = total_discount + discount_amount

    item_order = input("Do you want to enter another item? ")

print("The sum of all discounts is: $", format(total_discount, ".2f"))