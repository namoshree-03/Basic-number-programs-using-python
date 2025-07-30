#Armstrong number checker
num = int(input("Enter a number: "))
print("Original number:", num)
sum = 0
temp = num
while temp > 0:
    digit = temp % 10 # Get the last digit
    sum += digit ** 3 # Cube the digit and add to sum
    temp //= 10 # Remove the last digit
if sum == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
# This code checks if a number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# The user is prompted to enter a number, and the program checks if it is an Armstrong number.