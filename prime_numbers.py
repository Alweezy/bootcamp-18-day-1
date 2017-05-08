def is_prime(number):
    if number is 1:
        return False
    for value in range(2, int(number ** 0.5) + 1):
        if number % value is 0:
            return False
        return True

