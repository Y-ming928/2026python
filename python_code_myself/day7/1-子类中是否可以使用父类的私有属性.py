# 私有属性只能在自己的类中使用，子类也不能使用父类的私有属性
class A:
    def __init__(self):
        self.__age = 18

    def base_age(self):
        print(self.__age)


class B(A):
    def get_age(self):
        print(self.__age)
    def get_age1(self):
        self.base_age()

if __name__ == '__main__':
    zhangsan = B()
    zhangsan.get_age1()