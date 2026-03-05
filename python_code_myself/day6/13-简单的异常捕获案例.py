import test_exception_module
def use_exception1():
    try:
        num = int(input('请输入一个整数'))
        print(num)
    except:
        print('输入的必须是整型数字')

def use_exception2():
    """
    掌握异常的种类
    :return:
    """
    try:
        num = int(input('请输入整数'))
        result = 8/num
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('除以零错误')

def use_exception3():
    """
    掌握不同的异常类型，可以跳转到不同的分支上
    :return:
    """
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as e:  # e代表异常对象的别名
        print(e)


def use_exception4():
    """
    学习else和finally
    :return:
    """
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
        return
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("正常执行")
    finally:
        print("执行完成，但是不保证正确")  # 不受return影响

def use_exception5():
    """
    如何捕获异常发生的文件
    :return:
    """
    try:
        test_exception_module.test()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals['__file__']) # 异常发生的文件
        print(e.__traceback__.tb_lineno) # 异常发生的行号

if __name__ == '__main__':
    # use_exception3()
    use_exception5()
