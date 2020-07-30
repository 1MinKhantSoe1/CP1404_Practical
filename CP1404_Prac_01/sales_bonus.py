def main():

    sales = float(input("Enter sales: $"))

    while sales <= 0:  # while the number is negative

        print("Please enter sales again because your entered number is negative")
        sales = float(input("Enter sales: $"))

    while sales >= 0:  # while enter number is not negative

        if sales < 1000:  # if the sales amount under 1000 user will get 10% discount

            bonus = sales * 0.1

            print("{:.0f}".format(bonus))
            break

        else:  # if the sales amount over 1000 user will get 15% discount

            bonus = sales * 0.15

            print("{:.0f}".format(bonus))
            break

    return sales


if __name__ == '__main__':
    main()




