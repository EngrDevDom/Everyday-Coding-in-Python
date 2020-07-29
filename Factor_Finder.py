'''
    Factor Finder
        -> Ask the user to input an expression, calculate its factors and print them.
'''

from sympy import Symbol, solve, pprint

def find_factor(expr):
    t_expr = solve(expr, dict=True)
    pprint(t_expr)

if __name__ == '__main__':
    expr = input('Enter an expression in terms of x and y: ')
    find_factor(expr)

