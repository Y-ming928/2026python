class Cat(object):
    "这是一个猫类"
    def __init__(self,new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def eat(self):
        print(self.name + '爱吃鱼')

    def drink(self):
        print(self.name + '爱喝水')

    def __del__(self):  # 程序会自动销毁
        print(f'{self.name}猫对象被销毁')

    def __str__(self):
        """
        返回对象的信息
        :return:
        """
        return f'对象{self.name}'



def main():
    tom = Cat("张静")
    lazy_cat = Cat("苏启鸣")
    tom.name = '章敬'  # 不规范
    tom.eat()
    tom.drink()
    print(tom.name)
    print('-'*50)
    print(tom)
if __name__ == '__main__':
    main()
    print("程序结束")