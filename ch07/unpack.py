# Demonstration of unpacking arguments.
# A list or dictionary of values can be passed to a function as if they were
# normal positional or keyword arguments.

def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)


some_args = range(3)
more_args = {
    "arg1": "ONE",
    "arg2": "TWO"
}

print("Unpacking a sequence:", end=" ")
show_args(*some_args)

print("Unpacking a dict:", end=" ")
show_args(**more_args)
