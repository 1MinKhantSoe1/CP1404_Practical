HEX_COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb",
               "ANTIQUEWHITE2": "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378",
               "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "#458b74", "AZURE1": "#f0ffff"}

user_input = input("Enter Colour Name: ")

while user_input:

    converted_to_uppercase = user_input.upper()  # convert to uppercase

    if converted_to_uppercase not in HEX_COLOURS:

        print("Invalid colour name")

        user_input = input("Enter Colour Name: ")

    elif converted_to_uppercase in HEX_COLOURS:

        print(HEX_COLOURS[converted_to_uppercase])

        user_input = input("Enter Colour Name: ")

    else:

        break




