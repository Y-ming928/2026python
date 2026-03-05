import os

def use_name():
    os.rename('dir2','file4')

def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    # os.mkdir('dir3')  # 创建文件
    # os.rmdir('dir1')  # 删除文件
    print(os.getcwd())  # 当前工作目录
    os.chdir('dir2')    #修改当前目录
    file = open('file1','w',encoding='utf8')
    file.close()

def scan_dir(current_path,height):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' ' * height,file)  # 打印所有文件,height代表空格数
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path,height + 4)


if __name__ == '__main__':
    # use_name()
    # use_dir_func()
    scan_dir('.',0)