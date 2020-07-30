"""Password Check"""

def get_password(password):

    print("*" * len(password))


def main():

    password = input("Please Enter Your Password: ")

    get_password(password)


if __name__ == '__main__':
    main()