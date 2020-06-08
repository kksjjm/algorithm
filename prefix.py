class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for t in tokenList:
        if t == "(":
            opStack.push(t)
        elif t == ")":
            while opStack.peek() != "(":
                a = opStack.pop()
                postfixList.append(a)
            opStack.pop()
        else:
            if t in prec:
                if opStack.isEmpty():
                    opStack.push(t)
                else:
                    p = opStack.peek()
                    if prec[t] > prec[p]:
                        opStack.push(t)
                    else:
                        while not opStack.isEmpty() and prec[t] <= prec[p]:
                            b = opStack.pop()
                            postfixList.append(b)
                        opStack.push(t)
            else:
                postfixList.append(t)
                
    while not opStack.isEmpty():
        c = opStack.pop()
        postfixList.append(c)

    return postfixList


def postfixEval(tokenList):
    prec = ["+","-","*","/"]
    opStack = ArrayStack()
    val = []
    if tokenList:
        for t in tokenList:
            if not t in prec:
                opStack.push(t)
            else:
                c = 0
                a = opStack.pop()
                b = opStack.pop()
                if t == "+":
                    c = int(b) + int(a)
                elif t == "-":
                    c = int(b) - int(a)
                elif t == "*":
                    c = int(b)*int(a)
                else:
                    c = int(b)/int(a)
                opStack.push(c)
    val = opStack.pop()
    return val

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val