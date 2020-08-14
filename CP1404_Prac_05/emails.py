EMAIL = {"lindsay.ward@jcu.edu.au": "lindsay ward", "abe@gmail.com": "abe", "jimbo546@hotmail.com": "jimbo546"}

user_input = input("Email: ")

while user_input:

    if user_input in EMAIL:

        ques = input("Is your name {0} ? (Y/n) ".format(EMAIL[user_input].title()))

        if ques == "y" or ques == "":

            user_input = input("Email: ")

        else:

            name = input("Name: ")

            EMAIL[user_input] = name

            user_input = input("Email: ")

while user_input == "":

    print("")

    for key, value in EMAIL.items():

        print("{0:5} ({1})".format(value, key))

    break

