#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from stack import Stack

def divideBy2(decNumber):
    remStack = Stack()
    while decNumber > 0:
        remStack.push(decNumber%2)
        decNumber = decNumber // 2

    binString = ''
    while not remStack.isEmpty():
        binString += str(remStack.pop())

    return binString



def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remStack = Stack()
    while decNumber > 0:
        remStack.push(decNumber%base)
        decNumber = decNumber//base

    baseString = ''
    while not remStack.isEmpty():
        baseString = baseString + digits[remStack.pop()]

    return baseString


def test():
    print(divideBy2(8))
    print(divideBy2(23))
    print(baseConverter(25, 2))
    print(baseConverter(25, 7))
    print(baseConverter(255, 16))
    print(baseConverter(299, 8))
    print(baseConverter(300,16))

test()
