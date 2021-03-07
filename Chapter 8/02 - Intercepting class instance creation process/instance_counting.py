class InstanceCountingClass:
    created = 0
    number: int

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.number = cls.created
        cls.created += 1

        return instance

    def __repr__(self):
        return f"<{self.__class__.__name__}: " f"{self.number} of {self.created}>"


if __name__ == "__main__":
    instances = [InstanceCountingClass() for _ in range(5)]
    for i in instances:
        print(i)
    print(f"total: {InstanceCountingClass.created}")
