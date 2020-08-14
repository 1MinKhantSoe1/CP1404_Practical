STATE_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory"}
# print state name
print(STATE_NAME)


user_input = input("Please Enter short state name>>> ")

converted_to_uppercase = user_input.upper()  # convert to uppercase

print(STATE_NAME[converted_to_uppercase], "\n")

for key, value in STATE_NAME.items():

    print(key, "is", value)


