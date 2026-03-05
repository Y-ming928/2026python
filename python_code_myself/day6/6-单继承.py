class Animal:
    def __init__(self,name):
        self.name = name


    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)  # 子类对象调用父亲的init
        self.color = color

    def bark(self):
        print(f'{self.color}{self.name}狗叫')
        
    def run(self):
        super().run()
        print(f'{self.name}跑得快')

class xiaotiaoquan(Dog):
    def fly(self):
        print(f'{self.color}{self.name}飞天')

if __name__ == '__main__':
    wangcai = Dog('旺财','黑色')
    wangcai.bark()
    wangcai.run()
    xiaotian = xiaotiaoquan('哮天犬','绿色')
    xiaotian.fly()