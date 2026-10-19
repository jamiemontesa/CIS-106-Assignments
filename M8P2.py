# Jamie M8P2.py 10/18/2026

first = 1
second = 1

print("First 20 Fibonacci Numbers")

for count in range(20):
    print(first)

    next_number = first + second

    first = second
    second = next_number

