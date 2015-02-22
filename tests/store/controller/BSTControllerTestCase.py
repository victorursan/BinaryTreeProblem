__author__ = 'victor'

from unittest import TestCase
from store.domain.Node import Node
from store.controller.BSTController import BSTController
from store.repository.Repository import Repository


class BSTControllerTestCase(TestCase):
    def setUp(self):
        """
        set up the binary tree controller and inserting some data into repository
        """
        self.__repo = Repository()
        self.__repo.save(50)
        self.__repo.save(55)
        self.__repo.save(45)
        self.__ctrl = BSTController(self.__repo)

    def test_add_node(self):
        """
        test if the node is properly added
        """
        self.__ctrl.add_node(60)
        self.assertEqual(self.__ctrl.find_node(60), (Node(60), Node(55)))

    def test_remove_node(self):
        """
        test if the node is properly removed
        """
        self.__ctrl.remove_node(50)
        self.assertEqual(self.__ctrl.find_node(45), (Node(45), Node(55)))

    def test_find_node(self):
        """
        test if the node is found
        """
        self.assertEqual(self.__ctrl.find_node(45), (Node(45), Node(50)))

    def test_find_nodes_in_range(self):
        """
        test if the proper nodes are returned
        """
        self.assertEqual({n.data for n in self.__ctrl.find_nodes_in_range(10, 60)}, {45, 50, 55})

    def test_get_all_nodes(self):
        """
        test if tree has the corresponding nodes
        """
        self.assertEqual({n.data for n in self.__ctrl.get_all_nodes()}, {45, 50, 55})