class MusicPlayer:
    instance = None  # 用来保存对象的
    '''
        def __new__(cls, *args, **kwargs)是python自带的内置函数
        现将其修改，如果使得后续的所有对象的id均为同一个id
    '''
    def __new__(cls, *args, **kwargs):
        # 1、创建对象，分配空间,如果对象为空，为对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 父亲的new类似于c语言的malloc
        return cls.instance

    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    player1 = MusicPlayer('苏启鸣')
    player2 = MusicPlayer('章敬')  # 后面初始化对象就会将前面的给覆盖掉
    print(id(player1))
    print(id(player2))
    print(player1.name)
    print(player2.name)