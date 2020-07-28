'''
    Reading File : mydata.txt -> Calculate the Percentile
'''

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers

def calculate_percentile(numbers):
    n = len(numbers)
    i = (n*p)/100 + 0.5
    k = i*f
    f = 1/i
    percentile = (1-f)*data[k] + f*data[k+1]

    return percentile

if __name__ == '__main__':
    data = read_data('mydata.txt')
    percentile = calculate_percentile(data)
    print('Percentile: {0}'.format(percentile))

