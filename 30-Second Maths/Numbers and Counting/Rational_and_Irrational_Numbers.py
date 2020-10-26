num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

equiv1 = num1/num2
equiv2 = num2*equiv1

if equiv2 == num1:
    print('The numbers are rational.')
else:
    print('The numbers are irrational.')

