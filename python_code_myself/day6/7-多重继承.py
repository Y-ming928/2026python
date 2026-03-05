class A:
    def test(self):
        print('a test')

    def demo(self):
        print('a demo')

class B:
    def test1(self):
        print('b test')

    def demo(self):
        print('b demo')

class C(A,B):
    pass

if __name__ == '__main__':
    c = C()
    c.test1()