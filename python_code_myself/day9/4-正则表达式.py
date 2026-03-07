import re  # 正则表达式包

def simple():
    result = re.match('wangdao','wangdao.cn')
    if result:
        print(result.group())

def single():
    """
        匹配单个字符
        :return:
        """
    # .可以匹配任意一个字符
    ret = re.match(".", "M")
    print(ret.group())

    ret = re.match("t.o", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())

    print('-' * 50)
    # 大小写均可以匹配
    ret = re.match("[hH]","Hello python")
    print(ret.group())
    ret = re.match("[hH]","hello python")
    print(ret.group())

    # 匹配0~9
    ret = re.match("[0-9]hellopython","7hellopython")
    print(ret.group())
    ret = re.match("[0-35-9]hellopython","7hellopython")  # 0~9不要4进行匹配
    print(ret.group())

    print('-' * 50)
    ret = re.match("章敬\d号发射","章敬8号发射")  # \d匹配数字和【0-9】一样
    print(ret.group())

def more_alp():
      """
      匹配多个字符
      :return:
      """
      ret = re.match("[A-Z][a-z]*", "M")
      print(ret.group())

      ret = re.match("[A-Z][a-z]*", "MnnM")
      print(ret.group())

      ret = re.match("[A-Z][a-z]*", "Aabcdef")
      print(ret.group())
      print('-' * 50)
      names = ["name1", "_name", "2_name", "__name__"]
      for name in names:
          ret = re.match(r"[a-zA-Z_]\w*",name) # 开头必须是字母和下划线，后面可以为任意单个字符
          if ret:
              print(f'{name}是正确的')
          else:
              print(f'{name}不是正确的')
      print('-' * 50)
      #  ?是匹配一次或者不匹配
      ret = re.match(r"[1-9]?[0-9]", "7")
      print(ret.group())

      ret = re.match(r"[1-9]?\d", "33")
      print(ret.group())

      ret = re.match(r"[1-9]?\d", "09")
      print(ret.group())

      print('-' * 50)
      ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
      print(ret.group())
      ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")  # 贪婪的
      print(ret.group())

print('-'*50)
def start_end():
    """
    匹配结尾
    :return:
    """
    # 符合163的邮箱找出来
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r'\w{4,20}@163\.com$', email)  # 匹配的字符串中出现了正则的符号，要使用\进行转义
        if ret:
            print(f'{ret.group()}是正确的邮箱{email}')
        else:
            print(f'{email}邮箱地址不正确')
    # 匹配0-99
    ret = re.match("[1-9]?\d$","09")  # 是从末尾开始匹配的
    if ret:
        print(ret.group())
    else:
        print("不是1-99")

def split_group():
    ret = re.match("[1-9]?\d$|100", "100")  # 是从末尾开始匹配的
    if ret:
        print(ret.group())
    else:
        print("不是1-100")

    ret = re.match("[1-9]\d?","99")  # 匹配1-99
    if ret:
        print(ret.group())
    else:
        print("不是1-99")

    ret = re.match(r"\w{4,20}@(163|126|qq)\.com","test@126.com")  #()是让某个分组单独匹配的
    print(ret.group())
    print('-'*50)
    ret = re.match("([^-]*)-(\d*)","010-123456")  # （[^-]*）表示没有遇到-之前一直匹配
    # ^和[]在一起的组合式语法，其中()中的内容就是一个组别
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))

    print('-'*50)
    ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>")
    print(ret.group())
    ret = re.match(r"<[a-zA-Z]*>\w*</1>", "<html>hh</html>")  # </1>表示当前分组必须与前一个分组保持一致
    print(ret.group())

def other_func():
    """
    search findall sub split
    :return:
    """
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())
    print('-' * 50)
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")  # 拿出所有数字内容
    print(ret)

def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)  # 返回的是一个迭代器，这个迭代器可以使用next函数将里面的内容输出
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None

def use_findall():
    """

    :return:
    """
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)
    # findall 内部的设计机制，在分组前面加?:
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)
    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    # search 没问题
    ret1 = pattern1.search(ret_s)
    print(ret1.group())

def use_sub():
    long_text = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """
    # print(long_text)
    ret=re.sub(r'<[^>]*>|&nbsp;|\n|\s','',long_text)  # 将<内容>,&nbsp和换行、空格全部删掉
    print(ret)

def use_split():
    ret = re.split(r":| ","info:xiaoZhang 33 shandong")
    print(ret)

if __name__ == '__main__':
    # single()
    # more_alp()
    # start_end()
    # split_group()
    # other_func()
    # find_second_match()
    # text = "abc123def567ghi789"
    # pattern = r"\d+"
    # second_math = find_second_match(pattern, text)
    # print(second_math)
    # use_findall()
    # use_sub()
    use_split()