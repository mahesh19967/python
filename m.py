# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a number to calculate its factorial: "))

# Check if the number is non-negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
