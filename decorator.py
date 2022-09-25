class Myproperty():

    def __init__(self, fget=None, fset=None, fdel=None, doc=None) -> None:
        self.__fget = fget
        self.__fset = fset
        self.__fdel = fdel


    def __get__(self, obj, objtype):

        return self.__fget(obj)

    def __set__(self, obj, value):
        self.__fset(obj,value)

    def setter(self, fset):
        self.__fset = fset
        return self

class Person():
    def __init__(self,a) -> None:
        self._a = a

    @Myproperty
    def a(self):
        return self._a

    @a.setter
    def xxx(self, value):
        self._a = value


if __name__ == "__main__":
    stu = Person(3)
    print(stu.a)
    stu.a = 10
    print(stu.a)
