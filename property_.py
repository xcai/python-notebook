

class C:
    def __init__(self):
        self.__x = None

    def getx(self):
        print "got  ", self.__x
        return self.__x

    def setx(self, value):
        print "set  ", self.__x
        self.__x = value

    def delx(self):
        print "del ", self.__x
        del self.__x

    x = property(getx, setx, delx, 'i am property...')



c = C()
c.x = 100
y = c.x
print y
del c.x
print c.x