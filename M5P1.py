# Jamie M5P1.py 09/26/2026

# Input

quantity = int(input("quantity of item"))

# Processing

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

# Output

print(quantity)
print(unit_price)
print(extended_price)
print(tax)
print(total)
