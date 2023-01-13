# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
# Example 1:
# Input: "1 + 1"
# Output: 2
# Example 2:
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    class Token:
        pass

    def __init__(self):
        self.ARITHMETIC_OPERATORS = {'-': None, '+': None}
        self.OPEN_PARENTHESIS = '('
        self.CLOSING_PARENTHESIS = ')'
        self.SPACE = ' '
        self.PLUS = '+'
        self.MINUS = '-'

    def is_arithmetic_operator(self, char):
        return char in self.ARITHMETIC_OPERATORS

    def calculate_nested(self, operators, stack):
        sum = 0
        value = None
        while value != self.OPEN_PARENTHESIS:
            peek = len(operators) - 1
            symbol = operators[peek]
            if symbol == self.MINUS:
                operators.pop()
                value = stack.pop()
                if int(value) < 0 and symbol == self.MINUS:
                    sum += int(str(abs(value)))
                else:
                    sum += int(self.MINUS + str(value))
            elif symbol == self.PLUS:
                operators.pop()
                value = stack.pop()
                sum += int(str(value))
            elif symbol == self.OPEN_PARENTHESIS:
                value = stack.pop()
                if value == self.OPEN_PARENTHESIS:
                    stack.append(sum)
                    operators.pop()
                    return
                else:
                    sum += int(value)

    def get_number(self, idx, s):
        num = ''
        end = len(s)
        while idx != end:
            char = s[idx]
            if self.is_arithmetic_operator(char) or char == self.CLOSING_PARENTHESIS:
                break
            elif char != self.SPACE:
                num += char
            idx += 1
        return num, idx

    def calculate_result(self, operators, stack):
        sum = 0
        if len(stack) == 0:
            return None
        if len(stack) == 1:
            return int(stack[0])
        else:
            symbol = ''
            while len(stack) != 0:
                peek = len(operators) - 1
                if peek >= 0:
                    symbol = operators[peek]
                else:
                    symbol = '+'
                if symbol == self.MINUS:
                    operators.pop()
                    value = stack.pop()
                    if int(value) < 0 and symbol == self.MINUS:
                        sum += int(str(abs(value)))
                    else:
                        sum += int(self.MINUS + str(value))
                elif symbol == self.PLUS:
                    if operators:
                        operators.pop()
                    value = stack.pop()
                    sum += int(str(value))
        return sum

    def calculate(self, s: str) -> int:
        idx = 0
        end = len(s)
        operators = []
        stack = []
        while idx != end:
            char = s[idx]
            if char.isnumeric():
                num, i = self.get_number(idx, s)
                idx = i
                stack.append(num)
            elif self.is_arithmetic_operator(char):
                operators.append(char)
                idx += 1
            elif char == self.OPEN_PARENTHESIS:
                stack.append(char)
                operators.append(char)
                idx += 1
            elif char == self.CLOSING_PARENTHESIS:
                self.calculate_nested(operators, stack)
                idx += 1
            elif char == self.SPACE:
                idx += 1
        return self.calculate_result(operators, stack)


if __name__ == "__main__":
    solution = Solution()

    input_str = "(1-(3-4))"
    result = solution.calculate(input_str)
    assert result == 2

    input_str = "2-(5-6)"
    result = solution.calculate(input_str)
    assert result == 3

    input_str = '(1+(4+5+2)-3)+(6+8)'
    result = solution.calculate(input_str)
    assert result == 23

    input_str = '1 + 1'
    result = solution.calculate(input_str)
    assert result == 2

    input_str = ' 2-1 + 2 '
    result = solution.calculate(input_str)
    assert result == 3

    input_str = ' 11111  '
    result = solution.calculate(input_str)
    assert result == 11111

