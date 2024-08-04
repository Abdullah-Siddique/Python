def greet(name):
    return f"Hello, {name}!"

print(greet("Abdullah"))

def add(a, b):
    return a + b

print(add(5, 3))

def greet_with_default(name="Abdullah"):
    return f"Hello, {name}!"

print(greet_with_default())
print(greet_with_default("Sam"))

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(1, 2, 3, 4, 5))

def introduce(**kwargs):
    introduction = "This is "
    for key, value in kwargs.items():
        introduction += f"{key}: {value}, "
    return introduction[:-2]

print(introduce(name="Abdullah", age=17, profession="Student"))

def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")

square = lambda x: x * x
print(square(5))

def apply_function(func, value):
    return func(value)

print(apply_function(square, 6))

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

print(divide(10, 2))
print(divide(10, 0))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("John", 25)
print(person.introduce())

if __name__ == "__main__":
    print("This is the main function")
    print(greet("Anderson"))
