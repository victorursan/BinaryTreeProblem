__author__ = 'victor'

from store.repository.Repository import Repository
from store.domain.BinarySearchTree import BinarySearchTree


class BSTController(object):
    def __init__(self, repo: Repository):
        """ Initialize BSTController with the repo

        :param repo: the repository
        """
        self.__repo = repo
        self.__binarySTree = None
        self.__load_tree()

    def __load_tree(self):
        """ Loads all the data from the repository to the Tree
        """
        lst = self.__get_nodes_data()
        if len(lst) != 0:
            self.__binarySTree = BinarySearchTree(lst[0])
        if len(lst) > 1:
            for data in lst[1:]:
                self.__binarySTree.insert(data)

    def __get_nodes_data(self):
        """ Gets all the nodes data from the repo

        :return: a list of all nodes data
        """
        return self.__repo.get_all()

    def add_node(self, data):
        """ Add a node to the BinarySearchTree

        :param data: the data for the node
        """
        to_save = True
        if self.__binarySTree is None:
            self.__binarySTree = BinarySearchTree(data)
        else:
            to_save =  self.__binarySTree.search(data)[0] == None
            self.__binarySTree.insert(data)
        node = self.__binarySTree.search(data)[0]
        if to_save:
            self.__repo.save(node)

    def remove_node(self, data):
        """ Remove a node from the BinarySearchTree

        :param data: the data of the node we want to remove
        """
        if self.__binarySTree is not None:
            node = self.__binarySTree.search(data)[0]
            self.__binarySTree.delete(data)
            self.__repo.delete(node)
        else:
            print("Can't remove from an empty tree")

    def find_node(self, data):
        """ Finds the node with the specified data

        :param data: the data of the node we want to find
        :return: the node with the specified data
        """
        if self.__binarySTree is not None:
            return self.__binarySTree.search(data)
        return

    def find_nodes_in_range(self, low, high):
        """ Finds all nodes with the data between range(low, high+1)

        :param low: lower bound of the data
        :param high: higher bound of the data
        :return: a list of all nodes with the data between range(low, high+1)
        """
        if self.__binarySTree is not None:
            return self.__binarySTree.nodes_in_range(low, high)
        return None