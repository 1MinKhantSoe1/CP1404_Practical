user_input = input("Text: ")

print("Text: ", user_input)


count_word = {}

for word in user_input.split():

    if word in count_word:

        count_word[word] += 1

    else:

        count_word[word] = 1


for key, value in count_word.items():

    print("{0:10} : {1:10}".format(key, value))

