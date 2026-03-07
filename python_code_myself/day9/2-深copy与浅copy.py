import copy


def use_list_copy():  # 浅拷贝
    a = [1, 2, 3]
    b = a
    b[0] = 10  # a会发生变化
    print(a)
    b = a.copy()
    b[1] = 100
    print(a)
    print(b)

def use_copy():  # 深拷贝
    """
    使用copy中的copy
    :return:
    """
    c = [1,2,3]
    d = c
    print(id(c),id(d))   # id是相同的
    d = copy.copy((c))   # 复制自定义的对象的时候可以使用
    d[0] = 10
    print(c,d)

def use_copy2():
    a = [1,2]
    b = [3,4]
    c = [a,b]
    d = copy.copy(c)  # 浅拷贝是直接绑定的，前面改变，后面也接着该改变
    a[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)

def use_deep_copy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c),id(d))
    a[0] = 10
    print(c)
    print(d)

class Student:
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
        self.equipment = ['鞋子','指环']

def use_copy_own():
    old_hero = Student('章敬',90)
    new_hero = copy.copy(old_hero)
    new_hero.blood = 80
    new_hero.equipment.append('药水')
    print(old_hero.equipment)

if __name__ == '__main__':  # 深拷贝是新对象与旧对象之间完全分离的，浅拷贝新对象的可变数据发生了变化，旧对象也会发生变化
    # use_copy()            #但是浅拷贝不可变数据类型的改变不会影响旧对象的不可变数据类型
    # use_copy2()
    # use_deep_copy()
    use_copy_own()