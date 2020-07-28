'''
    The ratio between consecutive Fibonacci numbers approaches the golden ratio.
'''

import matplotlib.pyplot as plt

def fibo(n):

    # Algorithm
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    # n > 2
    a = 1
    b = 1

    # First two members of the series
    series = [a, b]
    a = b
    b = c

    return series

  # Set the label of each bar
    plt.xlabel('No.')
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers to Golden ratio')

    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()

# Run the main program
if __name__ == '__main__':

    n = 1

    fibo(n)
