import sys

"""
Demonstration of the command pattern.
"""


# Receiver classes
class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)


# Invoker classes
class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


# Command classes
class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()


# Demonstration of command pattern
def main():
    # Receiver objects
    window = Window()
    document = Document('a_document.txt')
    # Command objects
    save = SaveCommand(document)
    exit_cmd = ExitCommand(window)
    # Invoker objects with associated commands
    save_button = ToolbarButton('save', 'save.png')
    save_button.command = save
    save_keystroke = KeyboardShortcut('s', 'ctrl')
    save_keystroke.command = save
    exit_menu = MenuItem('File', 'Exit')
    exit_menu.command = exit_cmd

    # Save the document file and exit
    save_keystroke.keypress()
    exit_menu.click()


# Import guard
if __name__ == '__main__':
    main()
