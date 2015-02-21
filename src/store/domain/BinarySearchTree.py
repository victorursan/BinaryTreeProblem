__author__ = 'victor'

from store.domain.Node import Node


class BinarySearchTree(Node):
    def __init__(self, data):
        """ BinarySearchTree constructor

        :param data: node data object
        """
        super().__init__(data)

    def insert(self, data):
        """ Insert new node with data

        :param data: node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data, parent=None):
        """ Lookup node containing data

        :param data: node data object to look up
        :param parent: node's parent
        :returns: node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.search(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.search(data, self)
        return self, parent

    def delete(self, data):
        """ Delete node containing data

        :param data: node's content to delete
        """
        node, parent = self.search(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def children_count(self):
        """Return the number of children

        :returns: number of children (0, 1, 2)
        """
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count