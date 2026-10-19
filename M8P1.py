# JAMIE M8P1.py 10/16/2026


principal = float(input("Enter principal amount: "))
int_rate = float(input("Enter interest rate: "))

total_interest = 0

print()
print("Year     Beginning Balance     Ending Balance")

for year in range(1, 6):
    beginning_balance = principal

    interest = principal * int_rate
    ending_balance = principal + interest

    total_interest = total_interest + interest

    print(f"{year:<8} ${beginning_balance:>12,.2f}     ${ending_balance:>12,.2f}")

    principal = ending_balance

print()
print(f"Total interest earned: ${total_interest:,.2f}")

