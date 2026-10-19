# Jamie M8P3.py 10/18/2026

total_bonus = 0

file = open("Employees-M8P3.txt", "r")

print("Employee       Salary          Bonus")

for name in file:
    name = name.strip()
    salary = float(file.readline())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate

    total_bonus = total_bonus + bonus

    print(f"{name:<12} ${salary:>10,.2f}    ${bonus:>10,.2f}")

file.close()

print()
print(f"Total bonuses paid: ${total_bonus:,.2f}")

