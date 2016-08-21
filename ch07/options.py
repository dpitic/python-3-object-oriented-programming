# Demonstration of the use of keyword arguments.

class Options:
    """
    This class enables object initialisation with a set of options with default
    values.
    """

    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]


# Demonstration of class API
def main():
    options = Options(username="dusty", password="drowssap", debug=True)
    print("options['debug'] = {}".format(options['debug']))
    print("options['port'] = {}".format(options['port']))
    print("options['username'] = {}".format(options['username']))


# Import guard
if __name__ == '__main__':
    main()
