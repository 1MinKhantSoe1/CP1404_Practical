"""Broken Score"""


import random


def check_grade(result):

    if result < 0 or result > 100:

        result = "Invalid Grade"

    elif result >= 85:

        result = "Excellent"

    elif 65 <= result < 85:

        result = "Credit"

    elif 40 <= result < 65:

        result = "Pass"

    else:

        result = "Fail"

    return result


def main():

    score = int(input("Enter your score: "))
    result = check_grade(score)

    print(result)

    score1 = random.randint(1, 100)
    result1 = check_grade(score1)

    print(result1)


if __name__ == '__main__':
    main()