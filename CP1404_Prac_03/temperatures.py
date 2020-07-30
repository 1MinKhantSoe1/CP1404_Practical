"""Temperatures"""


def convert_celsius(fahrenheit):

    return 5 / 9 * (fahrenheit - 32)


def convert_fahrenheit (celsius):

    return celsius * 9.0 / 5 + 32


def main():

    print("C - For convert Celsius to Fahrenheit \n F - For convert Fahrenheit to Celsius")

    user_input = input("Choose One Option: ")

    if user_input.upper() == "C":

        celsius = float(input("Celsius: "))
        fahrenheit = convert_fahrenheit(celsius)

        print("result: {:.2f} F".format(fahrenheit))

    elif user_input.upper() == "F":

        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_celsius(fahrenheit)

        print("result: {:.2f} C".format(celsius))

    else:

        print("invalid")


if __name__ == '__main__':
    main()