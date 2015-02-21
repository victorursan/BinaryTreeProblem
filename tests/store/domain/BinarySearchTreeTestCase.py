__author__ = 'victor'

from unittest import TestCase
from store.domain.Node import Node


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