# File  :   Temp_convert.py
# Desc  :   A program to convert Celcius temps to Fahrenheit

def main():
    celcius = eval(input("What is the Celcius temperature? : "))
    fahrenheit = 9/5 * celcius + 32
    print("The temperature is ", fahrenheit, " degrees Fahrenheit")

main()
