def input_password():
    pwd = input("请输入密码: ")
    if len(pwd) >= 8:
        return pwd
    raise Exception("密码长度必须大于等于8位！")  # 抛出异常

if __name__ == '__main__':
    # try:
    #     input_password()
    # except Exception as e:
    #     print(e)
    try:
        assert 1==0,'你的程序在这里发生了什么异常'
    except Exception as e:
        print(e)