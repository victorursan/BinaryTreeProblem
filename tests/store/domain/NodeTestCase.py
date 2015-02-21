__author__ = 'victor'

from unittest import TestCase
from store.domain.Node import Node


class NodeTestCase(TestCase):
    def setUp(self):
        """
        set up the Node
        """
        self.node = Node(10)

    def test_data(self):
        """
        test if the Node's data is the expected one
        """
        self.assertEqual(self.node.data, 10)
        self.assertNotEqual(self.node.data, 5)

    def test_left(self):
        """
        set up the left Node and test the assignment
        """
        self.node.left = Node(5)
        self.assertEqual(self.node.left.data, 5)
        self.assertNotEqual(self.node.left.data, 10)

    def test_right(self):
        """
        set up the right Node and test the assignment
        """
        self.node.right = Node(15)
        self.assertEqual(self.node.right.data, 15)
        self.assertNotEqual(self.node.right.data, 20)

    def test_equal(self):
        """
        test if 2 nodes with the same values are equal
        """
        self.node.left = Node(5)
        self.node.right = Node(15)
        node2 = Node(10)
        node2.left = Node(5)
        node2.right = Node(15)
        self.assertEqual(self.node, node2)
        self.assertNotEqual(self.node, node2.right)
