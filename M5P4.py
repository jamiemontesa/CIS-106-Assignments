# Jamie M5P4.py 09/26/2026

# Input

appliance_name = input("appliance name")
cost_of_appliance = float(input("cost of appliance"))

# Processing

if cost_of_appliance > 1000.00:
    warranty_rate = 0.10
else:
    warranty_rate = 0.05

warranty_cost = cost_of_appliance * warranty_rate
total = cost_of_appliance + warranty_cost

# Output

print(appliance_name)
print(cost_of_appliance)
print(warranty_cost)
print(total)
