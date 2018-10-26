from functools import wraps
def a():
    print("Hi!")
    print("a!")
    print("bye")


def hi(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Hi")
        print(func.__name__)
        print("bye")
        return func(*args, **kwargs)
    return inner

@hi
def b():
    pass

a()
print("\n")
b()