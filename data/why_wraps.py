from functools import wraps

def without_wraps(func):
    """
    *args 파라미터를 몇 개를 받을지 몰라 사용, 튜플
    **kwargs 파라미터 명을 보낼 수 있음 딕셔너
    """
    def __wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return __wrapper

def with_wraps(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        #print("HI!!")
        return func(*args, **kwargs)
    return __wrapper

@without_wraps
def a():
    """func a"""
    return "a"

@with_wraps
def b():
    """func b """
    print("b!")
    return "bye"

print(a.__doc__)
print(a.__name__)
print(b.__doc__)
print(b.__name__)

print(b())