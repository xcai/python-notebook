


def say667():
    def saynum():
        print "in saynum:", num
    num = 666
    num += 1
    return saynum

temp = say667()

temp()
temp()
temp()