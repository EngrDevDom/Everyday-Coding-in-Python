'''
    Calculating the Median
'''

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    # Find the Median
    if N%2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1

        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N+1)/2

        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    return median

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    median = calculate_median(donations)
    N = len(donations)
    print('Median donations over the last {0} days is {1}'.format(N, median))

