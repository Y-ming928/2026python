class Person:
    """
        init是初始化属性的方法
    """
    def __init__(self,name,age,height):  #这个里面是传递过来的参数
        self.name = name  # self是对象的名字,self.name是对象的属性
        self.age = age
        self.height = height

    def run(self):
        print(self.name + '正在跑步')
        self.height -= 0.5
    def eat(self):
        print(self.name + '正在吃东西')
        self.height += 1

# 实例化
elphant = Person('大象',18,1.75)
tiger = Person('老虎',17,1.65)
elphant.run()
elphant.name = "章敬"
print(elphant.name,elphant.age,elphant.height)