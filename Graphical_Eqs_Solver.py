'''
    Graphical Equation Solver
        -> Asks the user for two expressions and graphs them both.
'''

from sympy import Symbol, sympify, solve
from sympy.plotting import plot

def plot_expression(expr1, expr2):
    x = Symbol('x')
    y = Symbol('y')
    p = plot(expr1, expr2, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()

if __name__ == '__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    plot_expression(expr1, expr2)

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)

