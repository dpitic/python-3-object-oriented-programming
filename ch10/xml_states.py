"""
Demonstration of the state pattern.

This code implements an XML parsing tool, where the context class will be the
parser itself. It will take a string as input and place the tool in an initial
parsing state. The various parsing states will consume characters, looking for
a specific value, and when that value is found, change to a different state.
The goal is to create a tree of node objects for each tag and its contents. To
simplify the implementation, this code will only parse a subset of XML; tags
and names. It can't handle attributes on tags. It will parse text content of
tags, but won't attempt to parse mixed content, which has tags inside of text.
"""


class Node:
    """
    The output of the parser is a tree of Node objects. The Node will need to
    know the name of the tag its parsing, and since it's a tree, it should
    maintain a pointer to the parent node and a list of the node's children in
    order. Some nodes have a text value, but not all of them.
    """

    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = ""

    def __str__(self):
        if self.text:
            return self.tag_name + ": " + self.text
        else:
            return self.tag_name


class FirstTag:
    """
    Initial state of the Parser. It finds the first tag.
    """
    def process(self, remaining_string, parser):
        """
        Process the remaining XML string using the parser and return what's
        left. This method sets the parser state to determine the next state.
        :param remaining_string: remaining XML string.
        :param parser: XML parser
        :return: the remaining XML string to parse.
        """
        # Find the index of the opening and closing angle brackets
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        # Get the tag name between opening and closing angle brackets
        tag_name = remaining_string[i_start_tag + 1:i_end_tag]
        # Create the root node based on the first tag name
        root = Node(tag_name)
        # The root node is also the current node
        parser.root = parser.current_node = root
        parser.state = ChildNode()  # Determine next transition state
        return remaining_string[i_end_tag + 1:]


class ChildNode:
    """
    Determine and set the parser the next state.
    """
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith('</'):
            parser.state = CloseTag()
        elif stripped.startswith('<'):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()
        return stripped     # string of text


class OpenTag:
    """
    This state adds the newly created node to the previous current node object's
    children and sets it as the new current node. The parser state is set back
    to the ChildNode state before continuing.
    """
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag+1:i_end_tag]
        node = Node(tag_name, parser.current_node)
        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()      # Determine next transition state
        return remaining_string[i_end_tag+1:]


class TextNode:
    """
    This state extracts the text before the next closing tag and sets it as a
    value on the current node.
    """
    def process(self, remaining_string, parser):
        # Find the end index of the closing tag
        i_start_tag = remaining_string.find('<')
        # Extract the text in this tag
        text = remaining_string[:i_start_tag]
        parser.current_node.text = text
        parser.state = ChildNode()      # Determine next transition state
        return remaining_string[i_start_tag:]


class CloseTag:
    """
    This state sets the parser's current node back to the parent node so any
    further children in the outside tag can be added to it.
    """
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        assert remaining_string[i_start_tag+1] == '/'
        tag_name = remaining_string[i_start_tag+2:i_end_tag]
        assert tag_name == parser.current_node.tag_name
        parser.current_node = parser.current_node.parent
        parser.state = ChildNode()      # Determine next transition state
        return remaining_string[i_end_tag+1:].strip()


class Parser:
    """
    The XML Parser will parse the XML string by transitioning to states which
    perform the parsing. It will start in a state where no nodes have yet
    been processed. It will have a state for processing opening and closing
    tags. It will also have a state for processing text inside a tag. The Parser
    will have a state to determine which state to transition to next, called the
    ChildNode transition state. The list of states are:
    FirstTag, ChildNode, OpenTag, CloseTag, Text
    The FirstTag state will switch to ChildNode, which will decide which of the
    other states to switch to. When those states are finished, they will switch
    back to the ChildNode state. The states are responsible for taking what's
    left of the string and processing as much of it as they know what to do
    with, and then telling the parser to handle the rest of it.
    """
    def __init__(self, parse_string):
        """
        Initialise the parser with the XML string to parse.
        :param parse_string: XML string to parse.
        """
        self.parse_string = parse_string
        self.root = None            # root XML node
        self.current_node = None    # node we are currently adding children to
        self.state = FirstTag()     # Parser state; start in initial state

    def process(self, remaining_string):
        """
        Process the remaining XML string by passing it off to the current
        Parser state, which is expected to return the remainder of the unparsed
        string when it has finished processing. The parser then recursively
        calls the process() method on this remaining string to construct the
        rest of the tree.
        :param remaining_string: remaining XML string
        :return: None
        """
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    if __name__ == '__main__':
        def start(self):
            self.process(self.parse_string)

# Test the API. Open a file from the command line, parse it and print the nodes
if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as file:
        contents = file.read()
        p = Parser(contents)
        p.start()

        nodes = [p.root]
        while nodes:
            node = nodes.pop(0)
            print(node)
            nodes = node.children + nodes
