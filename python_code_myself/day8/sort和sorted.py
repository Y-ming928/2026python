from operator import itemgetter,attrgetter

my_list = "This is a test string from Andrew".split()
print(my_list)

def chang_lower(str_name:str):
    return str_name.lower()

# 可以传递一个比较规则的函数，比较规则发生了变化
print(sorted(my_list,key=chang_lower))
print(my_list)  # sorted不会对原来的列表进行改变
# 比较规则发生的改变

my_list.sort(key=chang_lower)
print(my_list)  # sort会对原来的列表进行改变

print('-' * 50)
student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda x: x[2]))  # 匿名函数

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型，str是用来打印对象的返回对象的描述信息
        :return:
        """
        return repr((self.name, self.grade, self.age))

student = Student('john','A','12')

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
    ]
print(sorted(student_objects, key=lambda x: x.age))  # 匿名函数

print('-' * 50)
print(sorted(student_objects,key=lambda student:student.age))

print('使用operator系列')
print(sorted(student_tuples,key = itemgetter(2)))
print(sorted(student_objects,key = attrgetter('age')))

print('使用operator进行多列排序')
print(sorted(student_tuples,key = itemgetter(2,0)))  # 先按age排再按照name排
print(sorted(student_objects,key = attrgetter('grade','age')))

print('使用lambda表达式实现多列排序')
print(sorted(student_objects,key = lambda student:(student.grade,student.age)))
print(sorted(student_tuples,key = lambda x:(x[1],-x[2])))

mydict = { 'Li'   : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du'   : ['C',2],
           'Ma'   : ['C',9],
           'Zhe'  : ['H',7] }

print('-'*50)
print(sorted(mydict.items(),key = lambda x:x[1][1]))

gameresult = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
print('-'*50)
print(sorted(gameresult,key = lambda x:x['rating']))