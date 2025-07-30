#Prime number checker
import math
num = int(input("Enter a number: "))
print("Original number:", num)
if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")        