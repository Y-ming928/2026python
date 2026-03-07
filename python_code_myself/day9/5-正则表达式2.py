import re

def use_greedy():
    s = "This is a number 234-235-22-423"
    ret = re.match(r".+(\d+-\d+-\d+-\d+)", s)  # 贪婪，+号把234前面的23给吃了
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)",s)  # 非贪婪模式，在"*","?","+","{m,n}"后面加上？可以使得贪婪编程非贪婪
    print(ret.group(1))

    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))

def use_r():
    """
    r的作用, 原生字串
    :return:
    """
    mm = "c:\\a\\b\\c"
    print(mm)
    print(re.match(r"c:\\", mm).group())  # 如果不加r,则转译两个/则需要四个/，r代表原生字符串的意思

def use_option():
    print(re.match(r'\w*','abc函',flags=re.A).group())  # re.A不让\w匹配汉字
    print(re.match(r'a*', 'aA',flags=re.I).group())  # re.I不区分大小写
    print(re.match(r'.*','abc\ndef',flags=re.S).group())  # re.S可以让.匹配\n

if __name__ == '__main__':
    # use_greedy()
    # use_r()
    use_option()