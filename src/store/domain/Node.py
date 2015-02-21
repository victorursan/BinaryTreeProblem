__author__ = 'victor'


class Node(object):
    def __init__(self, data):
        """ Node constructor

        :param data: node data object
        """
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        """ Data property of the node

        :returns: node's data
        """
        return self.__data

    @property
    def left(self):
        """ Left branch of the node

        :returns: node's left child
        """
        return self.__left

    @property
    def right(self):
        """ Right branch of the node

        :returns: node's right child
        """
        return self.__right

    @data.setter
    def data(self, value):
        """ Data setter of the node

        :param value: node's new data object
        """
        self.__data = value

    @left.setter
    def left(self, node):
        """ Left branch setter of the node

        :param node: node's new left child
        """
        self.__left = node

    @right.setter
    def right(self, node):
        """ Right branch setter of the Node

        :param node: node's new right child
        """
        self.__right = node

    def __eq__(self, other):
        """ Checks if the 2 nodes have the same data object

        :param other: another node
        :returns: True if the nodes data are the same, otherwise False
        """
        if type(other) == Node:
            return self.data == other.data
        return False

    def __ne__(self, other):
        """ Checks if the 2 nodes don't have the same data object

        :param other: another node
        :returns: True if the nodes data are the different, otherwise False
        """
        return not self.__eq__(other)