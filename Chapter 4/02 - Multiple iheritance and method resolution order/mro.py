class CommonBase:
    pass


class Base1(CommonBase):
    pass


class Base2(CommonBase):
    def method(self):
        print("Base2.method() called")


class MyClass(Base1, Base2):
    pass


if __name__ == "__main__":
    print("MyClass's MRO:", MyClass.__mro__)
