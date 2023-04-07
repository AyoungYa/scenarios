def sum_of_squares(n: int) -> int:
    """Calculates the sum of the first n squares.

    Args:
        n (int): input number, e.g. 3

    Returns:
        result (int): 1^2 + 2^2 + 3^2 = 14
    """
    result = n * (n + 1) * (2 * n + 1) // 6
    return result
