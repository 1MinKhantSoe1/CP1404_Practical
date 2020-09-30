import doctest
from CP1404_Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""

    return " ".join([s] * n)


def is_long_word(word, length=5):
    """Determine if the word is as long or longer than the length passed in"""

    is_long_word("not")
    is_long_word("supercalifrag")
    is_long_word("Python", 6)
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""

    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test

    # TODO: 2. write assert statements to show if Car sets the fuel correctly

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()


# TODO: 4. Fix the failing is_long_word function

# TODO: 5. Write and test a function to format a phrase as a sentence,
def phrase_to_sentence(phrase):
    """Format a phrase as a sentence, starting with a capital and ending with a . """

    phrase_to_sentence('hello')
    phrase_to_sentence('It is an ex parrot.')
    phrase_to_sentence('This subject rocks')
    """capitalise the first letter"""
    sentence = phrase.capitalize()
    """add the full stop, but only if we need to"""
    if sentence[-1] != '.':
        sentence += '.'
    return sentence
