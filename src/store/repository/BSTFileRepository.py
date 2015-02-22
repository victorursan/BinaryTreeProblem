__author__ = 'victor'

from store.repository.Repository import Repository
from store.domain.Node import Node


class BSTFileRepository(Repository):
    def __init__(self, file_name):
        """ Initializes the  file repository

        :param file_name:
        :return:
        """
        Repository.__init__(self)
        self.__file_name = file_name
        self.__load_tree()

    def save(self, node: Node):
        """ Saves a new item in the repository and on file

        :param node: the new node that is added to repo and file
        """
        super().save(node.data)
        self.__save_node(node)

    def update(self, node1: Node, node2: Node):
        """ Updates and replaces a node with another one

        :param node1: the node we want to replace
        :param node2: the node with which we want to replace it
        """
        super().update(node1.data, node2.data)
        self.__update_file()

    def delete(self, node: Node):
        """ Deletes a node from the repo and file

        :param node: the node we want to remove
        """
        super().delete(node.data)
        self.__update_file()

    def __load_tree(self):
        """ Loads data from the file into the repo and BST
        """
        try:
            with open(self.__file_name, "r") as f:
                for line in f:
                    arr = line.split(", ")
                    for char in arr:
                        super().save(int(char))
        except Exception as ex:
            print("Error opening file {ex}".format(ex=ex))

    def __update_file(self):
        """ Updates the file with the new data
        """
        try:
            with open(self.__file_name, "w") as f:
                lst = self.get_all()
                for node_data in lst:
                    n = "{nod}, ".format(nod=node_data) if node_data != lst[-1] else str(node_data)
                    f.write(n)
        except Exception as ex:
            print("Error opening file {ex}".format(ex=ex))

    def __save_node(self, node: Node):
        """ Saves a new node on the file

        :param node: the node we want to add to the file
        """
        try:
            with open(self.__file_name, "a") as f:
                s = None
                if len(self.get_all()) != 0:
                    s = ", {nod}".format(nod=node.data)
                else:
                    s = "{nod}".format(nod=node.data)
                f.write(s)
        except Exception as ex:
            print("Error opening file {ex}".format(ex=ex))
