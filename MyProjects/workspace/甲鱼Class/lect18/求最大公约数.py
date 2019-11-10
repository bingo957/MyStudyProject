def gcd(x, y):
    """求最大公约数"""
    while y:
        t = x % y
        x = y
        y = t

    return x


print(gcd(4, 6))
