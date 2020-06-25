def addLayer(l):
    # generate the next layer
    l = [0] + l + [0]
    l2 = []

    for i in range(len(l) - 1):
        l2.append(l[i] + l[i+1])
    return l2

def problem(n):
    l = [[1]]

    # loop as many times as needed
    for _ in range(n):
        l.append(addLayer(l[-1]))

    # formatting the output
    length = len(' '. join(map(str, l[-1])))
    for li in l:
        row = ' '.join(map(str, li))
        while len(row) < length:
            row = ' ' + row + ' '

        print(row)

problem(20)

