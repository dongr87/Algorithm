from stack import Stack

def parChecker(symbolString):
    myStack = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol == '(':
            myStack.push(symbol)
        elif symbol == ')':
            if myStack.isEmpty():
                balanced = False
            else:
                myStack.pop()
        index += 1

    if balanced and myStack.isEmpty():
        return True
    else: return False

t1 = '(df((()df)))'
t2 = '(()((())()))'
t3 = '((dfdf((((())'
t4 = '))df)'

print(parChecker(t1))
print(parChecker(t2))
print(parChecker(t3))
print(parChecker(t4))
