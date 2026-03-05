class son1:
    def __init__(self,age,*args):
        self.age = age
        super().__init__(*args)

class son2:
    def __init__(self,score):
        self.score = score

class son(son1,son2):
    def __init__(self,name,*args):
        self.name = name
        super().__init__(*args)

if __name__ == '__main__':
    xiaoming = son('小明',18,92)
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(son.mro())