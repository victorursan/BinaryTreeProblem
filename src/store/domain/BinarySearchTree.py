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
        if self.data is not None:
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

    def nodes_in_range(self, low, high, lst=None):
        """ Searches for all nodes in range

        :param low: lower end of the range
        :param high: higher end of the range
        :param lst: list of nodes
        :returns: a list of nodes in range
        """
        if lst is None:
            lst = []
        if self.data in range(low, high + 1):
            lst.append(self)
            if self.left:
                self.left.nodes_in_range(low, high, lst)
            if self.right:
                self.right.nodes_in_range(low, high, lst)
        else:
            if low <= self.data and self.left:
                self.left.nodes_in_range(low, high, lst)
            if high >= self.data and self.right:
                self.right.nodes_in_range(low, high, lst)
        return lst

    def tree_nodes(self, lst=None):
        """ Returns all the nodes in the tree

        :return: all nodes in the tree
        """
        if lst is None:
            lst = []
        if self:
            lst.append(self)
        if self.left:
            self.left.tree_nodes(lst)
        if self.right:
            self.right.tree_nodes(lst)
        return lst

    def __str__(self):
        """ The string value of the node

        :return: the data of the node as string
        """
        return str(self.data)

    def __repr__(self):
        """ The representation of the node

        :return: the data of the node as string
        """
        return str(self.data)