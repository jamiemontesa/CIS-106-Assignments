# Jamie M7P4.py 10/07/2026

count = 0
total_pay = 0

employee = input("Do you want to enter an employee? ")

while employee == "yes":
    last_name = input("Enter the employee's last name: ")
    hours_worked = float(input ("Enter the amount of hours worked: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * pay_rate

    print("Employee's last name: ", last_name)
    print("The gross pay is: $", format(gross_pay, ".2f"))

    total_pay = total_pay + gross_pay
    count = count + 1

    employee = input("Would you like to enter another employee? ")

print("Total Gross Pay: $", format(total_pay, ".2f"))
print("Number of employees: ", count)

if count > 0:
    average_pay = total_pay / count
    print("Average Pay: $", format(average_pay, ".2f"))