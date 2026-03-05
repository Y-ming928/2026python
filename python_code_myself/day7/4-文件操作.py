def open_r():
    """
    读取文件
    :return:
    """
    file = open('file2.txt',mode='r',encoding='utf-8')
    text = file.read()
    print(text)
    file.close()

def open_rw():
    """
    读取文件
    :return:
    """
    file = open('file2.txt',mode='r+',encoding='utf-8')
    text = file.read()
    print(text)
    file.write('jjb')  # 写道文件末尾
    file.close()

def file3():
    file = open('dir2',mode='w',encoding='utf-8')  # 文件不存在就创建，存在就清空
    file.write('素琴名，张江')
    file.close()

def open_a():
    """
    练习a模式，每次写的时候写到文件末尾,相当于append
    :return:
    """
    file = open('dir2',mode='a+',encoding='utf-8')
    file.write('aaa')  # 使用r+模式，打开后光标在开头，内容直接覆盖
                        #  使用a+模式，打开后光标在末尾

def use_readline():
    file = open('dir2',encoding='utf-8')
    while True:
        # 读取一行内容
        text = file.readline()
        # 判断是否读取到内容，读取到文件末尾拿到的是一个空字符串
        if not text:
            break
        print(text,end="")
    file.close()

if __name__ == '__main__':
    # open_r()
    # open_rw()
    # dir3()
    # open_a()
    use_readline()