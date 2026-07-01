
# 1. Sum of Digits of a NumberThis program extracts each digit of the number
# using the modulo operator (%) and sums them up.


num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits =", total)



# 2. Reverse a Number
# This program reverses the digits of the given number.


num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)


# 3. Armstrong Number Check


num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



# 4. Prime Number Check


num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")



# 5. Prime Numbers in a Range


start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
