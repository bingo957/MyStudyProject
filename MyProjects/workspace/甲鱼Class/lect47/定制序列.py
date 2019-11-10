class CountList(list):
    """
    0.根据课堂上的例子,定制一个列表,同样要求记录列表中每个元素被访问的次数。这一次我们希里定制的列表功
    能更加全面一些,比如支持 append0、pop0、 extend0原生列表所拥有的方法。你应该如何修改呢?
    要求1:实现获取、设置和删除一个元素的行为(删除一个元素的时候对应的计数器也会被删除)
    要求2:增加 counter(ndex)方法,返回 index参数所指定的元素记录的访问次数
    要求3:实现 append0、pop0、 remove、 insert0、 clearl0和 reverse0方法(重写这些方法的时候注意考虑计数的对应改变)
    """

    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        while args:
            self.count.append(0)
            
    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
