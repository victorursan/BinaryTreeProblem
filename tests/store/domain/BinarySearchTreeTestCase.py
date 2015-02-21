__author__ = 'victor'

from unittest import TestCase
from store.domain.Node import Node
from store.domain.BinarySearchTree import BinarySearchTree


class BinarySearchTreeTestCase(TestCase):
    def setUp(self):
        """
        set up the binary tree and inserting some nodes
        """
        self.bst = BinarySearchTree(50)
        self.bst.insert(17)
        self.bst.insert(72)
        self.bst.insert(12)
        self.bst.insert(23)
        self.bst.insert(54)
        self.bst.insert(76)
        self.bst.insert(9)
        self.bst.insert(14)
        self.bst.insert(19)
        self.bst.insert(67)

    def test_insert(self):
        """
        test if the node is properly inserted
        """
        self.assertEqual(self.bst.left.data, 17)
        self.assertEqual(self.bst.right.data, 72)
        self.assertEqual(self.bst.left.left.data, 12)

    def test_search(self):
        """
        test if the search function returns the proper node and parent node
        """
        self.assertEqual(self.bst.search(19), (Node(19), Node(23)))
        self.assertEqual(self.bst.search(50), (Node(50), None))
        self.assertEqual(self.bst.search(68), (None, None))

    def test_delete(self):
        """
        test if the delete function deletes the node and fixes the successor parent issue
        """
        self.bst.delete(72)
        self.assertEqual(self.bst.search(54), (Node(54), Node(76)))
        self.bst.delete(50)
        self.assertEqual(self.bst.search(76), (Node(76), Node(54)))

    def test_children_count(self):
        """
        test if the node has the corresponding number of children
        """
        self.assertEqual(self.bst.children_count(), 2)
        self.assertEqual(self.bst.left.right.children_count(), 1)

    def test_nodes_in_range(self):
        """
        test if the nodes between the range are the expected ones
        """
        self.assertEqual({n.data for n in self.bst.nodes_in_range(10, 60)}, {50, 12, 17, 14, 23, 54, 19})
