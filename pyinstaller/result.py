# -*- coding: UTF-8 -*-
import re
ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
 
def middle_to_after(s):
    expression = []
    ops = []
    ss = s.split(' ')
    for item in ss:
        if item in ['+', '-', '*', '/']:
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(item)
                    break
                op = ops.pop()
                if op == '(' or ops_rule[item] > ops_rule[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    expression.append(op)
        elif item == '(':
            ops.append(item)
        elif item == ')':
            while len(ops) > 0:
                op = ops.pop()
                if op == '(':
                    break
                else:
                    expression.append(op)
        else:
            expression.append(item)
 
    while len(ops) > 0:
        expression.append(ops.pop())
 
    return expression

def expression_to_value(expression):
    stack_value = []
    for item in expression:
        if item in ['+', '-', '*', '/']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            result = cal(n1, n2, item)
            stack_value.append(result)
        else:
            stack_value.append(int(item))
    return stack_value[0]
 
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
 
if __name__ == '__main__':
    expression = middle_to_after('9 + ( 3 * ( 4 - 2 ) ) * 3 + 10 / 2')
    value = expression_to_value(expression)
    print (value)
    phone = "13098921645"
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    is_phone = re.search(phone_pat, phone) 
    if is_phone:
        print(phone)