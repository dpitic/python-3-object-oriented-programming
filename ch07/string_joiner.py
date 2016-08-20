import random, string

# Demonstration of context managers.

class StringJoiner(list):
    """
    Context manager used to construct a sequence of characters and convert it
    to a string upon exit.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.result = "".join(self)


# Demonstration of class API
def main():
    # Construct a string of 15 random characters
    with StringJoiner() as joiner:
        for i in range(15):
            joiner.append(random.choice(string.ascii_letters))

    print(joiner.result)


if __name__ == '__main__':
    main()
