import math
from typing import Callable, Dict, Union

def pow_op(base: float, exponent: float) -> float:
    return float(math.pow(base, exponent))

def fib_op(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial_op(n: int) -> int:
    return math.factorial(n)

def sqrt_op(x: float) -> float:
    return math.sqrt(x)

OPERATION_REGISTRY: Dict[str, Callable[..., Union[int, float]]] = {
    "pow": pow_op,
    "fib": fib_op,
    "factorial": factorial_op,
    "sqrt": sqrt_op,
}
