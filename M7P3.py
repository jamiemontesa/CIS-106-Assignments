# Jamie M7P3.py 10/07/2026

count = 0

prompt = input("Do you want to enter a student? ")

while prompt == "yes":
    last_name = input("Enter the student's last name ")
    exam_one = float(input("Enter the first exam score "))
    exam_two = float(input("Enter the second exam score "))

    average_score = (exam_one + exam_two) / 2

    print("Last Name: ", last_name)
    print("Average Score is: ", average_score)

    count =  count +1

    prompt = input("Would you like to enter another student? ")

print("Number of students entered: ", count)