"""
Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.

Example

For a = 2, b = 3, and c = 5, the output should be
arithmeticExpression(a, b, c) = true.
"""
def arithmeticExpression(a, b, c):
    if a+b==c or a-b==c or a/b==c or a*b==c:
        return True
    return False

