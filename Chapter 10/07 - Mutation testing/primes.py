def is_prime(number):
    if not isinstance(number, int) or number < 0:
        return False

    if number in (0, 1):
        return False

    for element in range(2, number):
        if number % element == 0:
            return False
    return True
