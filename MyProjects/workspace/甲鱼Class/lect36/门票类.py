"""
平日票价100元
周末票价为平日120%
儿童半价
"""


class Ticket:
    def __init__(self, weekend=False, ischild=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if ischild:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_price(self, num):
        return self.exp * self.inc * self.discount * num


adult = Ticket()
child = Ticket(ischild=True)
print("2个成年人和1个小孩的平日票价为：%.2f" % (adult.cal_price(2) + child.cal_price(1)))
