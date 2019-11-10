"""
游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。(初学者不一定可以完整实现，但请务必先自己
动手，你会从中学习到很多知识的^^)
·假设游戏场景为范围(xy)为0<=x<=10,0<=y<=10
·游戏生成1只乌龟和10条鱼
·它们的移动方向均随机
·乌龟的最大移动能力是2(Ta可以随机选择1还是2移动)，鱼儿的最大移动能力是1
·当移动到场景边缘，自动向反方向移动
·乌龟初始化体力为100(上限)
·乌龟每移动一次，体力消耗1
·当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
·鱼暂不计算体力
·当乌龟体力值为0(挂掉)或者鱼儿的数量为0游戏结束

"""
import random as r

legal_x = [0, 10]
legal_y = [0, 10]


class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])


    def move(self):
        # 随机计算方向并移动到新位置
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景X边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景X边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 体力减一
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)


    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])


    def move(self):
        # 随机计算方向并移动到新位置
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景X边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景X边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 体力减一
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼吃完了，游戏结束！')
        break
    if not turtle.power:
        print('乌龟体力耗完了，挂掉了！')
        break

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器直接引用列表数据使用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除就不会出现问题
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            # 鱼被吃掉了
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃掉了！')
