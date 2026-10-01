# Jamie M6P1 09/30/2026

# Input

quantity = int(input("Quantity of widgets: "))

# Processing

if quantity > 10000:
    price = 10.00

elif quantity >= 5000:
    price = 20.00

else:
    price = 30.00

extended_price = quantity * price

tax_amount = extended_price * 0.07

total = extended_price + tax_amount

# Output

print(f"Extended Price:  ${extended_price:,.2f}")
print(f"Tax Amount:      ${tax_amount:,.2f}")
print(f"Total:           ${total:,.2f}")
