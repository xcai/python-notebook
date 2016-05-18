

class Decorator1(object):

    def __init__(self, func):
        print '__init__    get function: ', func
        self.func = func

    def __call__(self, *args, **kwargs):
        print "__call__    before run ", self.func
        self.func(*args, **kwargs)
        print "__call__    after run ", self.func


@Decorator1
def greet(name, say='hello '):
    print say, name


greet('cosmo')


print '*'*40

class Decorator2(object):

    def __init__(self, *arg):
        print "get decorator arguments: ", arg
        self.todo = arg

    def __call__(self, f):
        print "inside  ", f
        print self.todo

        def wrapper(*args):
            print "get ", f, " args ", args, " before running"
            f(*args)
            print "finished ", f

        return wrapper


@Decorator2('have ', 'a ', 'drink')
def eat(food):
    print "start to eat ", food


eat('rice')
