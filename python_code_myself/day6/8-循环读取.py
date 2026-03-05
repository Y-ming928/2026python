# 如果要一次性读取多个
num = input()
my_list = [int(x) for x in num.split()]
print(my_list)