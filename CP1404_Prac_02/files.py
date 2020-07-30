"""
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
"""
"""Start"""

output_file = open("name.txt", "w")  # create and write the new text file

name = input("Enter your name: ")

print(name, file=output_file)

output_file.close()

""" End (Ques 1) """

"""
2. Write code that opens "name.txt" and reads the name (as above) then prints, 
   Your name is Bob" (or whatever the name is in the file).
"""
"""Start"""

read_file = open("name.txt", "r")

read_name = read_file.read()

print("Your name is {}".format(read_name))

""" End (Ques 2) """


"""
3. Create a text file called numbers.txt and save it in your prac_02 directory. 
   Put the following three numbers on separate lines in the file and save it:
   17
   42
   400
   Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, 
   which should be... 59.
"""
"""Start"""

read_number_file = open("numbers.txt", "r")

read_first_number = int(read_number_file.readline())
read_second_number = int(read_number_file.readline())

result = read_first_number + read_second_number

print(result)

read_number_file.close()

""" End (Ques 3) """

print()

"""
4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of 
   numbers.
"""
"""Start"""

total = 0

number_file = open("numbers.txt", "r")

read_number = number_file.readlines()

for line in read_number:

    change_str_to_int = int(line)

    total += change_str_to_int

print(total)

number_file.close()

""" End (Ques 4)"""


