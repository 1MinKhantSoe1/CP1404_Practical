"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: when user enter alphabet instead of number the ValueError is occur.
2. When will a ZeroDivisionError occur?
Ans: when user enter zero for denominator the ZeroDivisionError occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
For question number 3, I made a few changes to code that will be ask you again and again when user enter 0 for
denominator. I think that can avoid from ZeroDivisionError.
"""


try:

    zero_division_error = False

    while not zero_division_error:

        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator != 0:
            fraction = numerator / denominator
            print(fraction)
            zero_division_error = True


except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
