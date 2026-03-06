import sys
sys.setrecursionlimit(10000)
def sum_numbers(num):
    print(num)

    # 递归的出口（结束条件）
    if num == 1:
        return
    sum_numbers(num-1)

sum_numbers(3)

# 1.找到递归公式
# 2.编写结束条件

n = int(input("请输入台阶数："))
def step(n):
    if n == 1 or n == 2: return n
    else: return step(n-1) + step(n-2)

print(step(n))