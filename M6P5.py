# Jamie M6P5 10/01/2026

# Input

last_name = input("Enter last name: ")
salary = float(input("Enter salary: $"))
job_level= int(input("Job level: "))

# Processing

if job_level >= 10:
    bonus_rate = 0.25

elif job_level >= 5:
    bonus_rate = 0.20

else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

# Output

print("\nLast name:", last_name)
print(f"Bonus:     ${bonus:,.2f}")