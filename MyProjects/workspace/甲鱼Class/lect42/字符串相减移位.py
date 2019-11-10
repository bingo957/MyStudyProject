class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')
    def __lshift__(self, other):
        return self[other:] + self[:other]
    def __rshift__(self, other):
        return self[:-other] + self[-other:]
