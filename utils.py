def factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
