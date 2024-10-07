from typing import Callable


class LazyProperty:
    def __init__(self, method: Callable) -> None:
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls) -> object:
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @LazyProperty
    def resource(self) -> int:
        print("loading data from expensive resource")
        return ["a", "lot", "of", "objects", "from", "the", "database"]


def main():
    print(Test)
    t = Test(1, 10)
    print(t.resource)
    print(t.resource)


if __name__ == "__main__":
    main()
