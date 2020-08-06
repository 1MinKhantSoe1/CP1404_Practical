numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] -> Ans: 3
# numbers[-1] -> Ans: 2
# numbers[3] -> Ans: 1
# numbers[:-1] -> Ans: [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> Ans: [1]
# 5 in numbers -> Ans: True
# 7 in numbers -> Ans: False
# "3" in numbers -> Ans: False
# numbers + [6, 5, 3] -> Ans: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"  # Change the first element of numbers to "ten" (the string, not the number 10)

numbers[-1] = 1  # Change the last element of numbers to 1

print(numbers[2:])  # Get all the elements from numbers except the first two (slice)

print(9 in numbers)  # Check if 9 is an element of numbers
