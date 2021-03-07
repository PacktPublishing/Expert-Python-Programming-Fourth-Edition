class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Updating", self.name)
        self.val = val

    def __delete__(self, obj):
        print("Deleting", self.name)


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


if __name__ == "__main__":
    m = MyClass()
    m.x
    m.x = 20
    m.x
    del m.x
