"""
Go实现版本

https://tour.go-zh.org/methods/12
https://go.dev/tour/methods/12

~/Development/ws_go/learngo/tour/generics/index.go
"""
# Python 里类似的泛型函数可以用 typing.Generic
from typing import TypeVar, List, Optional

T = TypeVar('T')

def index(lst: List[T], x: T) -> Optional[int]:
    for i, v in enumerate(lst):
        if v == x:
            return i
    return -1

# 使用
print(index([10, 20, 15, -10], 15))  # 2
print(index(["foo", "bar", "baz"], "hello"))  # -1