# Jamie M8P5.py 10/18/2026

total_tuition = 0
student_count = 0

file = open("students.txt", "r")

print("Student       Credits       Tuition")

for name in file:
    name = name.strip()
    district = file.readline().strip()
    credits = int(file.readline())

    if district == "I":
        cost_per_credit = 250
    else:
        cost_per_credit = 500

    tuition = credits * cost_per_credit

    total_tuition = total_tuition + tuition
    student_count = student_count + 1

    print(f"{name:<12} {credits:<10} ${tuition:>10,.2f}")

file.close()

print()
print(f"Total tuition owed: ${total_tuition:,.2f}")
print(f"Number of students: {student_count}")

