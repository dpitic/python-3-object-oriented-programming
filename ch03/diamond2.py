class BaseClass:
    """
    Base class for demonstrating the diamond problem of multiple inheritance.
    This time using calls to super(), which calls the next method in the
    inheritance hierarchy.  This is not necessarily the parent class, especially
    in multiple inheritance situations.
    """
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

def main():
    s = Subclass()
    s.call_me()
    # Using super(), the base class is only called once because super() calls
    # the next method in the class heirarchy, which is not always the parent
    # class, especially in multiple inheritance situations.
    print("Sub calls   = %d\nLeft calls  = %d\nRight calls = %d\n"
        "Base calls  = %d" % (s.num_sub_calls, s.num_left_calls,
        s.num_right_calls, s.num_base_calls))

if __name__ == '__main__':
    main()
