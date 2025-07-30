#Palindrome Number Checker
num = int(input("Enter a number: "))
print("Original number:", num)
temp = num
rev = 0
while temp>0:
    digit = temp % 10  # Get the last digit
    rev = rev * 10 + digit  # Build the reversed number
    temp //= 10  # Remove the last digit
if rev == num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
# This code checks if a number is a palindrome.
# A palindrome is a number that remains the same when its digits are reversed.
# The user is prompted to enter a number, and the program checks if it is a palindrome.
