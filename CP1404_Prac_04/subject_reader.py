def main():

    display_subject_detail(get_data())


def get_data():

    read_file = open("subject_data.txt", "r")
    new_data = []

    for line in read_file:

        line = line.strip()  # Remove "\n"
        parts = line.split(',')     # Separate data
        parts[2] = int(parts[2])    # Convert to integer
        new_data.append(parts)

    read_file.close()
    return new_data


def display_subject_detail(new_data):

    for detail in new_data:

        print("{0} is taught by {1} and has {2} students.".format(*detail))


if __name__ == '__main__':
    main()