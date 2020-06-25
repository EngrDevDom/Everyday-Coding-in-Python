# File  :   Temp_convert.py
# Desc  :   A program to convert Celcius temps to Fahrenheit Version 2.0
#           This version issues heat and cold warningws.

def main():
    celsius = float(input("What is the Celsius temperature? : "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    elif fahrenheit < 30:
        print("Brrr... Be sure to dress warmly!")

main()
