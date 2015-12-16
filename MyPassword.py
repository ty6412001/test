#encoding=utf-8

#=========================================================================
#                           v1.0
#=========================================================================

def getRegix(fileName):
    """
    :return list of regix
    """
    a = []
    with open(fileName) as _file :
        i = 0
        for _line in _file.readlines():
            words = _line[:-1].split(" ")
            a.append(words)
            i += 1
        pass
        print a
    return a
    pass

def searchWords(regix,str):
    """
    :param regix:  str:need to search
    :return: num of col and row
    """
    for x in range(len(regix)):
        for y in range(len(regix[x])):
            if str == regix[x][y]:
                return (x,y)
            pass
        pass
    raise NameError, "no such str"
    pass


def calcuate(regix):
    x = regix[0]
    y = regix[1]
    for i in range(32):
        for k in range(32):
            print  (x<<i)|(y<<k)
            pass
        pass
    pass

def getXandY(number):
    for x in range(4):
        for y in range(10):
            if number == ((x<<5) | (y<<6)):
                print x,y
                pass
            pass
        pass
    pass


if __name__ == '__main__':
    a = getRegix("Test")
    b = searchWords(a,"66")
    print b
    #calcuate(b)
    print u"你好"
    print (3<<5)|(7<<6)
    getXandY(480)