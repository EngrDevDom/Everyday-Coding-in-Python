n = eval(input("Enter size of box: "))
for i in range(n):
    if i % (n-1) == 0:  print('*'*n)
    else:   print('*' + ' '*(n-2) + '*')