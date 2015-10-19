# Commentary: __new__ method(static method: decoration is not needed) takes the
# class *object* as first argument. Generally used for subclassing immutable
# types

def deco(cls):
    instance = {}
    def wrapper(*args):
        if cls not in instance:
            instance[cls] = cls(*args)
            return instance[cls]
        return instance[cls]
    return wrapper


class Singleton:
    instance = None

    def __new__(cls, x):
        print(type(cls))
        if not Singleton.instance:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance


s = Singleton(2)
# t = Singleton()
# print(s is t)


@deco
class Test:
    pass
t = Test()
t2 = Test()

@deco
class Foo:
    pass

f= Foo()
f2 = Foo()


d = {Singleton: 'a'}
