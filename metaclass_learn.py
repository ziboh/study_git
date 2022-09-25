class meta(type):
    def __get__(self, obj, obtype):
        return '自定义原类get'
 
class A(metaclass = meta):
    name = meta("hh",(),{})
    
print(A.name)
print(A)

B=A
print(B)
a = A()
print(a.name)


class Person:
    def __init__(self) -> None:
        pass
        print(super().__init__)
    def __method(self):
        pass
    def eat(self):
        return self.__init__
        
if __name__ == "__main__":
    pass