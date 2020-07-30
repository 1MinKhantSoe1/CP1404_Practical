def main():

    for i in range(1, 21, 2):

        print(i, end=' ')

    print()

    for i in range(0, 10+1):  # count in 10s from 0 to 100

        print(i*10, end=' ')

    print()

    for i in range(20, 0, -1):  # count down from 20 to 1

        print(i, end=' ')

    print()

    number_of_stars = int(input("Number of stars : "))  # ask the user for a number

    for i in range(0, number_of_stars):  # then print the *

        print("*", end='')

    print()

    for i in range(0, number_of_stars+1):  # print n lines of increasing stars.

        print("*" * i)

    print()


if __name__ == '__main__':
    main()