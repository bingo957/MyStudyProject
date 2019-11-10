class Nint(int):
    """继承int当传入字符串时返回ASCII码的和"""
    def __new__(cls, arg):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
            # return total
        return int.__new__(cls, arg)
