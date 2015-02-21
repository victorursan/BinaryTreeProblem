__author__ = 'victor'


class Node(object):
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @data.setter
    def data(self, value):
        self.__data = value

    @left.setter
    def left(self, node):
        self.__left = node

    @right.setter
    def right(self, node):
        self.__right = node

    def __eq__(self, other):
        if type(other) == Node:
            return self.data == other.data
        return False

    def __ne__(self, other):
        return not self.__eq__(other)