"""
例如将12345分解为【1，2，3，4，5】
"""


def get_digits(num):
    if num > 0:
        result.insert(0, num % 10)
        get_digits(num // 10)
    return result


result = []
print(get_digits(12345))
