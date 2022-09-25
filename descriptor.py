class A:
    def __get__(self, obj, type=None):
        return "get", self, obj, type


class B(metaclass=type):
    name = A()


b = B()
print(b.name)
print(B.name)
def a(): return 1


print(a)