def sum_of_cubes(n: int) -> int:
    """Calculates the sum of the first n cubes.

    Args:
        n (int): input number, e.g. 3

    Returns:
        result (int): 1^3 + 2^3 + 3^3 = 36
    """
    result = (n * (n + 1) // 2) ** 2
    return result
