# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md

def printline(func):
    def wrapper(*args, **kwargs):
        print("="*50)
        res = func(*args, **kwargs)
        print("="*50)
        print()
        return res
    return wrapper

@printline
def printdoc(func):
    print(func.__doc__)

printdoc(abs)
printdoc(int)
printdoc(str)
printdoc(input)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''
    return n**p

printdoc(pow)
print(pow(3, 4))
