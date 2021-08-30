test = '1 + 2 * 3 + 4 * 5 + 6'

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
            while operator and operator[-1]!='(':
                output.append(operator.pop())
            operator.append(token)
        elif token == '+':
            while operator and operator[-1] not in ['(', '*']:
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


# homework = map(parse_expression, open('input.txt', 'r').read().splitlines())
# print(f'Part 1: {sum(map(lambda s: rpn(shunting_yard_2(s)), homework))}')

print(rpn(shunting_yard_2(parse_expression(test))))
