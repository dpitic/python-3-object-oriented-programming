class BaseClass:
    """
    Base class for demonstrating the diamond problem of multiple inheritance.
    This is a naive implementation where the base class is called twice.
    """
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        BaseClass.call_me(self)
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("Calling method on Subclass")
        self.num_sub_calls += 1

def main():
    s = Subclass()
    s.call_me()
    # Expect the base class to be called twice
    print("Sub calls   = %d\nLeft calls  = %d\nRight calls = %d\n"
        "Base calls  = %d" % (s.num_sub_calls, s.num_left_calls,
        s.num_right_calls, s.num_base_calls))

if __name__ == '__main__':
    main()
