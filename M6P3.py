# Jamie M6P3 09/30/2026

# Input

principle = float(input("The principle amount is: "))
years_to_maturity = int(input("Years to maturity: "))

# Processing

if principle > 100000 and years_to_maturity == 5:
    interest_rate = 0.06

elif principle >= 50000 and principle <= 100000 and years == 10:
    interest_rate = 0.05

elif principle >= 50000 and principle <= 100000 and years == 5:
    interest_rate = 0.04

else:
    interest_rate = 0.02

interest = principle *  interest_rate

# Output

print("\nPrinciple:          $", format(principle, ",.2f"))
print(f"Interest Rate:      {interest_rate: .2%}")
print(f"First Year Interest: ${interest:,.2f}")