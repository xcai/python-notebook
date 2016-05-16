

import yaml


class Singleton(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


a = Singleton()
b = Singleton()
c = Singleton()

assert a is b is c



class SingletonMeta(type):
    def __init__(cls, name, bases, dict):
        super(SingletonMeta, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance


class MyClass(object):
    __metaclass__ = SingletonMeta


assert MyClass() is MyClass() is MyClass()

