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
    Initial state of the Parser.
    """
    def process(self, remaining_string, parser):
        i_start_tag = remaining_string.find('<')
        i_end_tag = remaining_string.find('>')
        tag_name = remaining_string[i_start_tag + 1:i_end_tag]
        root = Node(tag_name)
        parser.root = parser.current_node = root
        parser.state = ChildNode()  # Determine next transition state
        return remaining_string[i_end_tag + 1:]


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

    def start(self):
        self.process(self.parse_string)
