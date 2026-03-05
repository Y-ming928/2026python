import os
def seek_start():
    """
    相对于开头进行偏移
    :return:
    """
    file = open('dir2',mode='r+',encoding='utf8')
    file.seek(5,os.SEEK_SET)  #相对于开头移动五个字节
    text = file.read(5)
    print(text)
    file.close()

def seek_end():
    """
    相对于尾部进行偏移
    :return:
    """
    file = open('dir2', mode='rb+', encoding='utf8')
    file.seek(-6, os.SEEK_END)
    text = file.read(5)
    print(text)  # 读不到内容，是空字符串
    file.close()

def seek_b_cur():
    """
    在b模式下，读取到的是字节流，读取图片，音频，视频
    :return:
    """
    file = open('file1', mode='rb+')
    file.seek(5, os.SEEK_CUR)
    file.seek(-2, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    b = file.read()  # 得到的是字节流
    print(b)
    file.close()

def copty_file():  # 进行复制
    file1 = open('baidu.png',mode='rb+')
    file2 = open('baidu_copy.png',mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()

def modify_movie():  #可以取反某个字节来躲避检查
    with open('baidu.png', 'rb+') as file1:
        file1.seek(10, os.SEEK_SET)

        b = file1.read(1)          # 读1字节
        print("原字节:", b)

        value = b[0]               # 取出整数值
        new_value = 255 - value    # 取反

        file1.seek(10, os.SEEK_SET)   # 回到原位置
        file1.write(bytes([new_value]))

        print("修改后字节:", bytes([new_value]))


if __name__ == '__main__':
    # seek_start()
    # seek_b_cur()
    # copty_file()
    modify_movie()