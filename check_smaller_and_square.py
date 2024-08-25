# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Determine the smaller and larger number
if num1 < num2:
    smaller = num1
    larger = num2
else:
    smaller = num2
    larger = num1

# Output the smaller number
print(f"The smaller number is: {smaller}")

# Check if the larger number is the square of the smaller number
if larger == smaller ** 2:
    print(f"The larger number {larger} is the square of the smaller number {smaller}.")
else:
    print(f"The larger number {larger} is not the square of the smaller number {smaller}.")
