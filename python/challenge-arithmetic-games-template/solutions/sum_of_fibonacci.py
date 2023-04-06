def sum_of_fibonacci(n: int) -> int:
    """Generates the sum of the first n Fibonacci terms.

    Args:
        n (int): input number, e.g. 3

    Returns:
        result (int): 0 + 1 + 1 = 2
    """
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        print(fib)
        result = sum(fib)

    return result
