class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())


class A:
    pass

class B:
    def process(self):
        print('B process()')


class C(A, B):
    pass

class D(C, B):
    pass

obj_1 = D()
obj_1.process()
print(D.mro())
