"""Головний скрипт, що демонструє імпорт функцій із модуля lib."""
 
from lib import add, multiply, greet
 
 
def main() -> None:
    """Викликає функції з lib та виводить результати їхньої роботи."""
    print(greet("світ"))
    print("2 + 3 =", add(2, 3))
    print("4 * 5 =", multiply(4, 5))
 
 
if __name__ == "__main__":
    main()