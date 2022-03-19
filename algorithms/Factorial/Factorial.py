def factorial(n: int) -> float:
    """
    Given a positive integer, calculate its factorial
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')

    if n < 0:
        raise ValueError("n must be positive")

    if n == 0:
        return 1

    return n * factorial(n - 1)