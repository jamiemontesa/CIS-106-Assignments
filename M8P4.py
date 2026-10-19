# Jamie M8P4.py 10/18/2026

total_price = 0
order_count = 0

file = open("orders.txt", "r")

print("Item         Quantity      Price      Extended Price")

for item in file:
    item = item.strip()
    quantity = int(file.readline())
    price = float(file.readline())

    extended_price = quantity * price

    total_price = total_price + extended_price
    order_count = order_count + 1

    print(f"{item:<12} {quantity:<10} ${price:>8,.2f}    ${extended_price:>10,.2f}")

file.close()

if order_count > 0:
    average_order = total_price / order_count
else:
    average_order = 0

print()
print(f"Total extended price: ${total_price:,.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order: ${average_order:,.2f}")
