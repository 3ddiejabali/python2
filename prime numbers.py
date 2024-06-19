def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check divisibility from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Example usage:
number_to_check = int(input("Enter a number: "))
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
