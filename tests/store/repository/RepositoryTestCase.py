__author__ = 'victor'

from unittest import TestCase
from store.domain.Node import Node


class RepositoryTestCase(TestCase):
    def setUp(self):
        """
        setting up the repository and saving some Nodes
        """
        self.__repo = Repository()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        self.__repo.save(n1)
        self.__repo.save(n2)
        self.__repo.save(n3)

    def test_size(self):
        """
        test the size of the repo
        """
        self.assertEqual(self.__repo.size(), 3)

    def test_get_all(self):
        """
        test if the list saved in the repo
        """
        l = self.__repo.get_all()
        self.assertEqual(len(l), 3)

    def test_save(self):
        """
        test the save method of the repo
        """
        n = Node(4)
        self.__repo.save(n)
        self.assertEqual(self.__repo.size(), 4)

    def test_delete(self):
        """
        test the delete method of the repo
        """
        self.__repo.delete(Node(1))
        self.assertEqual(self.__repo.size(), 2)

    def test_find(self):
        """
        test the find method of the repo
        """
        n = self.__repo.find(Node(1))
        self.assertEqual(n, 0)

    def test_update(self):
        """
        test the update method of the repo
        """
        self.__repo.update(Node(1), Node(4))
        self.assertEqual(self.__repo.find(Node(4)), 0)