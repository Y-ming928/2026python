
# 多指参数就是参数个数不确定，必须是下面的写法
# *args就是一个元组拆包，**kwargs就是一个字典拆包,num就是一个元素
def demo(num,*args,**kwargs):
    print(num)
    print(args)
    demo2(*args,**kwargs)  # 用*args和**akwargs来进行传递参数
    # 如果不加*和**，则把args和kwargs对应的元组和字典看成一个参数



def demo2(*args,**kwargs):
    print(f'demo2:{args}')
    print(f'demo2{kwargs}')

demo(1,"dw",3,4,5,name = '小明',age = 19)

