def gcd(a, b):
    """
    Returns the greatest common divisor (GCD) of a and b using Euclid's algorithm.
    """
    while b != 0:
        # calculate remainder of a divided by b
        r = a % b

        # set a to b and b to the remainder
        a = b
        b = r

    return a
