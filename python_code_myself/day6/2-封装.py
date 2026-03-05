class Person:
    """人类"""

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步了，减重0.5kg,现有体重{self.weight}kg')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃饭了，增加0.5kg,现有体重{self.weight}kg')

    def __str__(self):
        return f"我的名字叫{self.name},体重为{self.weight}kg"

if __name__ == '__main__':
    elephant = Person('大象',80)
    elephant.run()
    elephant.eat()
    print(elephant)