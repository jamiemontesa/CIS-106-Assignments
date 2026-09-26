# Jamie M5P5.py 09/26/2026

# Input

last_name = input("last name")
dependents = int(input("number of dependents"))
gross_income = float(input("gross income"))

# Processing

adj_gross_income = gross_income - (dependents * 12000)

if adj_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adj_gross_income * tax_rate

if income_tax < 0:
    income_tax = 100

# Output

print(last_name)
print(gross_income)
print(dependents)
print(adj_gross_income)
print(income_tax)