def print_info(name, title="", gender=True):
    """
        :param title: 职位
        :param name: 班上同学的姓名
        :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (title, name, gender_text))

print_info("小明")
print_info("老王", title="班长",gender = False)
print_info("小美", gender=False)