'''
    Calculating the Mean
'''

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)

    # Calculate the Mean
    mean = s/N

    return mean

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean donation over the last {0} days is {1}'.format(N, mean))

