"""Модуль з допоміжними функціями для демонстрації імпорту в Python."""
 
 
def add(a: float, b: float) -> float:
    """Повертає суму двох чисел a та b."""
    return a + b
 
 
def multiply(a: float, b: float) -> float:
    """Повертає добуток двох чисел a та b."""
    return a * b
 
 
def greet(name: str) -> str:
    """Формує та повертає рядок-привітання для заданого імені name."""
    return f"Привіт, {name}!"