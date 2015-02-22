__author__ = 'victor'

from store.controller.BSTController import BSTController


class Console(object):
    def __init__(self, bst_controller: BSTController):
        """ Set's up the controller for the console

        :param bst_controller: the BinarySearchTreeController
        """
        self.__bst_controller = bst_controller

    def __ui_add(self, *args):
        """ Adds nodes to the BST via the controller

        :param args: data to be added to the BST
        """
        if len(args) < 1:
            print("To few arguments")
        elif len(args) >= 1:
            for arg in args:
                self.__bst_controller.add_node(arg)

    def __ui_remove(self, *args):
        """ Removes nodes from the BST via the controller

        :param args: data to be removed from the BST
        """
        if len(args) < 1:
            print("To few arguments")
        elif len(args) >= 1:
            for arg in args:
                self.__bst_controller.remove_node(arg)

    def __ui_find(self, *args):
        """ Finds a node in the BST

        :param args: the data we have to find in BST
        """
        if len(args) < 1:
            print("To few arguments")
        elif len(args) > 1:
            print("To many arguments")
        else:
            node, parent = self.__bst_controller.find_node(args[0])
            print("node data:{node} \nparent data:{parent}".format(node=node, parent=parent))

    def __ui_find_in_range(self, *args):
        """ Finds all nodes between a range

        :param args: contains the lower and upper bound of the range
        """
        if len(args) < 2:
            print("To few arguments")
        elif len(args) > 2:
            print("To many arguments")
        else:
            print(self.__bst_controller.find_nodes_in_range(args[0], args[1]))

    def run(self):
        """ Prints the menu with the options
        """
        options = {"add": self.__ui_add, "remove": self.__ui_remove, "find": self.__ui_find,
                   "range": self.__ui_find_in_range}
        while True:
            print("\nOptions:\n1. add <data>\n2. remove <data>\n3. find <data>\n"
                  "4. range <low_bound> <high_bound>\n5. exit\n")
            inp = input("> ").strip()
            if inp == "exit":
                break
            else:
                inp = inp.split(" ")
                try:
                    args = [int(a) for a in inp[1:]]
                    options[inp[0]](*args)
                except KeyError:
                    print("Option wasn't implemented")
                except ValueError:
                    print("Data should be numbers")