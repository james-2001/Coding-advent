from typing import List


test = '2 * 3 + (4 * 5)'


def parse_expression(expression: str) -> list[str]:
    return list(expression.replace(" ", ""))


def shunting_yard_1(expression: list[str]):
    output = []
    operator = []
    while expression:
        token = expression.pop(0)
        if token.isdigit():
            output.append(token)
        elif token in ['+', '*']:
            while operator and operator[-1] != '(':
                output.append(operator.pop())
            operator.append(token)
        elif token == '(':
            operator.append(token)
        elif token == ')':
            while operator[-1] != '(':
                output.append(operator.pop())
            operator.pop()
    output += operator
    return output


def shunting_yard_2(expression: list[str]):
    output = []
    operator = []
    while expression:
        token = expression.pop(0)
        if token.isdigit():
            output.append(token)
        elif token == '*':
            while operator and operator[-1] != '(':
                output.append(operator.pop())
            operator.append(token)
        elif token in ['+', '(']:
            operator.append(token)
        elif token == ')':
            while operator[-1] != '(':
                output.append(operator.pop())
            operator.pop()
    while operator:
        output.append(operator.pop())
    return output


def rpn(expression: list[str]):
    output = []
    while expression:
        token = expression.pop(0)
        if token.isdigit():
            output.append(token)
        elif token == '+':
            x = int(output.pop())
            y = int(output.pop())
            output.append(x+y)
        elif token == '*':
            x = int(output.pop())
            y = int(output.pop())
            output.append(x*y)
    return output.pop()
s="""4 * (7 * 2 * 6 * 2 + 6 * (5 + 3)) * (2 + 5 * 5 * 3) + (7 * 7 + (7 + 6) * 5 * 6) * (4 + (3 + 4) + 4 * 5 * (5 
+ 4 * 9 * 7 * 9 * 6))"""
print(rpn(shunting_yard_1(parse_expression(s))))
homework = map(parse_expression, open('input.txt', 'r').read().splitlines())
print(sum(map(lambda s: rpn(shunting_yard_2(s)), homework)))
