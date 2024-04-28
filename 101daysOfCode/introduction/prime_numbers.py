# Write your code below this line 👇


def prime_checker(number):
    if number in (2, 3):
        print(f"It's a prime number.")
        return
    if number % 2 == 0 or number == 1:
        print(f"It's not a prime number.")
        return

    i = 2
    prime = True

    while i <= number / 2:
        if number % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
