'''
    Generating Equally Spaced Floating Point Numbers
'''

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers
