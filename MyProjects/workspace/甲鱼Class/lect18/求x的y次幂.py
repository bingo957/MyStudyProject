def pow(x, y):
    """求x的y次幂"""
    result = 1
    for i in range(y):
        result *= x
    return result


print(pow(2, 3))
