import wikipedia


def search_WIKIPEDIA():

    search = input("Enter search >>>> ")

    while search:

        print(wikipedia.summary(search))
        page = wikipedia.page(search)
        print("Page Title:", page.title)
        print("Page URl:", page.url)
        print("Page Content:", page.content)
        print("Page Image:", page.images[0])
        print("Page Link:", page.links[0])
        print("")

        print("If you want to quit, type Q")
        search_phrase = input("Enter search: ")

        if search_phrase.upper() == "Q":
            print("Thank you!")
            break

        return search_phrase


search_WIKIPEDIA()
