"""My first exercise in COMP110!"""

__author__ = "730678627"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet(name="Student")
greet(name="Enlee")
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
