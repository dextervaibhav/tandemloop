

class Calculator:

    operand1 = None
    operand2 = None
    operator = None

    def __init__(self,op1,op2,o):
        self.operand1 = op1
        self.operand2 = op2
        self.operator = o


    def operation(self):
        if self.operator=='+':
            return float(self.operand1+self.operand2)
        elif self.operator=='-':
            return float(self.operand1-self.operand2)
        elif self.operator=='/':
            return float(self.operand1/self.operand2)
        elif self.operator=='*':
            return float(self.operand1*self.operand2)




while True:

    inp = list(input('Enter your inputs: ').split())
    p = float(inp[0])
    q = float(inp[1])
    r = inp[2]
    c = Calculator(p,q,r)
    print('ans:', c.operation())

