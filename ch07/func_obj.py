# Demonstration that functions in Python are objects. Consequently, they can
# have attributes set (not common to do so), and they can be passed around to
# other functions to be called at a later date. They also have a few special
# properties that can be accessed directly.


def my_function():
    print("The Function Was Called")


my_function.description = "A silly function"


def second_function():
    print("The second was called")


second_function.description = "A sillier function."


def another_function(function):
    print("The description:", end=" ")
    print(function.description)
    print("The name:", end=" ")
    print(function.__name__)
    print("The class:", end=" ")
    print(function.__class__)
    print("Now I'll call the function passed in")
    function()


another_function(my_function)
another_function(second_function)
