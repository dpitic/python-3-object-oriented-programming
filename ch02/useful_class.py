class UsefulClass(object):
    """
    Demonstration of the __name__ and __main__ concept. Ensures the module
    is not run when imported.
    """
    pass

def main():
    """
    Define the main function to run when the module is loaded by the
    interpreter. This function should not run when the module is imported.
    """
    useful = UsefulClass()
    print(useful)

# Script guard to ensure the script is not executed when imported by another
# module. The script should only be executed if it is loaded by the Python
# interpreter.
if __name__ == '__main__':
    main()    
