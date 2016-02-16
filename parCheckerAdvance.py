from stack import Stack

def parChecker(symbolString):
    myStack = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            myStack.push(symbol)
        elif symbol in ')]}':
            if myStack.isEmpty():
                balanced = False
            else:
                top = myStack.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and myStack.isEmpty():
        return True
    else:
        return False





def matches(open, close):
    openList = '([{'
    closeList = ')]}'
    return openList.index(open) == closeList.index(close)

def test():
    t1 = '{{([][])}()}'
    t2 = '[{()]'
    t3 = '{asd[df(fsd)d]}sdfoi'
    print(parChecker(t1))
    print(parChecker(t2))
    print(parChecker(t3))

test()
