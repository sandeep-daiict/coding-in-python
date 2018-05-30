#https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression/0
#code
import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv } 
t = int(input())
while t > 0:
    t = t - 1
    expr = input()
    stack = []
    val=0
    for c in expr:
        if c.isdigit():
           stack.append(int(c)) 
        else:
            if len(stack) > 1:
                a=stack[-1]
                b=stack[-2]
                stack=stack[:-2]
                val = int(ops[c](b,a))
                stack.append(val)
    print(stack[0])
