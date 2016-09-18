import json


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)


class ContactEncoder(json.JSONEncoder):
    """
    Custom contact encoder.
    """

    def default(self, obj):
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'first': obj.first,
                    'last': obj.last,
                    'full': obj.full_name}
        return super().default(obj)


def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic


def main():
    c = Contact("John", "Smith")
    print(json.dumps(c, cls=ContactEncoder))

    data = ('{"is_contact": true, "last": "smith",'
            '"full": "john smith", "first": "john"}')
    c = json.loads(data, object_hook=decode_contact)
    print(c)
    print("Full name = {}".format(c.full_name))


if __name__ == '__main__':
    main()
