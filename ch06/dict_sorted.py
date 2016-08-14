from collections import KeysView, ItemsView, ValuesView

# This is an incomplete implementation of a sorted dictionary.

class DictSorted(dict):
    """A dictionary that remembers the order in which keys were inserted."""

    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        # Use a list (mutable, ordered) to store the keys.
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        """self[key] = value syntax"""
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def __iter__(self):
        """for x in self syntax"""
        return self.ordered_keys.__iter__()


# Demonstration of class API
def main():
    ds = DictSorted()
    d = {}
    ds['a'] = 1
    ds['b'] = 2
    ds.setdefault('c', 3)
    d['a'] = 1
    d['b'] = 2
    d.setdefault('c', 3)
    for k, v in ds.items():
        print(k, v)
    for k, v in d.items():
        print(k, v)


# Import guard
if __name__ == '__main__':
    main()
