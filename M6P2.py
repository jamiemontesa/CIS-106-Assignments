# Jamie M6P2 09/30/2026

# Input

part_number = input("Part number: ")
quantity = int(input("Quantity: "))

# Processing 

if part_number == "10" or part_number == "55":
    unit_cost = 1.00

elif part_number == "99":
    unit_cost = 2.00

elif part_number == "80" or part_number == "70":
    unit_cost = 3.00

else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

# Output

print("\nPart Number:    ", part_number)
print(f"Cost per unit:   ${unit_cost:,.2f}")
print(f"Total cost:      ${total_cost:,.2f}")
