# Jamie M5P3.py 09/26/2026

# Input

number_of_books = int(input("number of books"))
cost_per_book = float(input("cost per book"))

# Processing

order_total = number_of_books * cost_per_book

if order_total > 50.00:
    shipping_charge = 0
else:
    shipping_charge = 25.00

# Output

print(order_total)
print(shipping_charge)
