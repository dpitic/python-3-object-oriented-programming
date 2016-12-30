"""
Demonstration of the composite design pattern.

The composite pattern is used to build complex tree-like structures from simple
components. The components, called composite objects, are able to behave like
a container and like a variable, depending on whether they have children
components. Composite objects are container objects, where the content may be
another composite object.

Normally, each component in a composite object must be either a leaf node (that
cannot contain other objects) or a composite node. The key is that both the
composite and leaf nodes can have the same interface.

This script uses the composite pattern to model a filesystem hierarchy
consisting of folders and files.
"""


class Component:
    """
    Component is the superclass in the composite design pattern. This class has
    the common attributes and operations.
    """
    def __init__(self, name):
        self.name = name

    def move(self, new_path):
        """
        Move this Component to the new path.
        :param new_path: destination path string where to move this Component to
        :return: None
        """
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        """
        Delete this Component from the tree.
        :return: None
        """
        del self.parent.children[self.name]


class Folder(Component):
    """
    Folder Component can have children. This is a composite component.
    """
    def __init__(self, name):
        """
        Initialise a new Folder composite Component which holds children in a
        dictionary. The dictionary enables us to look up children by name.
        :param name: name of this Folder Component.
        """
        super().__init__(name)
        self.children = {}      # Folder can have children composite components

    def add_child(self, child):
        """
        Add a child Component to this Folder Component.
        :param child: child Component to add to this Folder.
        :return: None
        """
        child.parent = self
        self.children[child.name] = child

    def copy(self, new_path):
        pass


class File(Component):
    """
    File Component is a leaf.
    """
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

    def copy(self, new_path):
        pass


# Root folder
root = Folder('')


def get_path(path):
    """
    Return the nodes in the given path separated by '/', similar to Unix paths.
    :param path: path string of nodes separated by '/'
    :return: nodes in the given path string
    """
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node


# Demonstration of API
def main():
    folder1 = Folder('folder1')
    folder2 = Folder('folder2')
    root.add_child(folder1)
    root.add_child(folder2)
    folder11 = Folder('folder11')
    folder1.add_child(folder11)
    file111 = File('file111', 'contents')
    folder11.add_child(file111)
    file21 = File('file21', 'other contents')
    folder2.add_child(file21)
    print('Folder 2 children {}'.format(folder2.children))
    print('move folder2 to /folder1/folder11')
    folder2.move('/folder1/folder11')
    print('Folder 11 children {}'.format(folder11.children))
    print('move file21 to /folder1')
    file21.move('/folder1')
    print('Folder 1 children {}'.format(folder1.children))


# Import guard
if __name__ == '__main__':
    main()
