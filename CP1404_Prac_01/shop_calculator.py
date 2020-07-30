def main():

    total_price = 0

    number_of_items = int(input("Number of items : "))  # ask user for number of items

    for i in range(0, number_of_items):  # loop depends for number of items

        price_of_item = float(input("Price of item : "))

        total_price += price_of_item  # total price of items

    if total_price > 100:  # if items are over $100 they will get 10% discount

        discount = total_price * 0.1

        total_discount_price = total_price - discount

        print("Total price for {0:.0f} is ${1:.2f}".format(number_of_items, total_discount_price))

    else:

        print("Total price for {0:.0f} is ${1:.2f}".format(number_of_items, total_price))


if __name__ == '__main__':
    main()