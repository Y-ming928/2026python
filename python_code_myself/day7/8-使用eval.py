def read_conf():
    """
    读取配置
    :return:
    """
    file = open('file6','r+',encoding='utf8')
    text_info = file.read()
    print(text_info)
    my_dict = eval(text_info)  # eval就是用来都配置的
    print(my_dict['ip'])

if __name__ == '__main__':
    read_conf()