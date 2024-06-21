from typing import Callable, Optional

def greet(name: str) -> str:
    return f"Hello, {name}!"

def repeat(func: Callable[[str], str], times: Optional[int] = 1) -> None:
    for _ in range(times):
        print(func("Alice"))

repeat(greet, 3)
