# calable objects with __call__ 

from typing import Any


class A:

    def __init__(self, x) -> None:
        print("init")
        self.x=x

    def __call__(self, y) -> None:
        print("__call__")
        self.y=y

obj = A(2)
print(obj.x)



obj(6)

print(obj.y)

print(obj.__dict__)