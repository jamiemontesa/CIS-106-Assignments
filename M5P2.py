# Jamie M5P2.py 09/26/2026

# Input

item_name = input("item name")
quantity = int(input("quantity"))

# Processing

if item_name == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price

# Output

print(item_name)
print(unit_price)
print(extended_price)

