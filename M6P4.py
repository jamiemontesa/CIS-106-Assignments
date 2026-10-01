# Jamie M6P4 10/01/2026

#Input

quantity = int(input("Quantity of concert tickets: "))

# Processing

if quantity >= 25:
    price = 50.00

elif quantity >= 10:
    price = 60.00

elif quantity >= 5:
    price = 70.00

else:
    price = 75.00

total_cost = quantity * price

# Output

print("\nQuantity of tickets: ", quantity)
print(f"Price per ticket:     ${price:,.2f}")
print(f"Total cost:           ${total_cost:,.2f}")