from store.domain.Node import Node

__author__ = 'victor'

from store.repository.Repository import Repository


class BSTFileRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name
        self.__load_tree()

    def save(self, item):
        super().save(item)
        self.__save_node(item)

    def update(self, item1, item2):
        super().update(item1, item2)
        self.__update_file()

    def delete(self, item):
        super().delete(item)
        self.__update_file()

    def __load_tree(self):
        try:
            with open(self.__file_name, "r") as f:
                for line in f:
                    arr = line.split(", ")
                    for char in arr:
                        n = Node(int(char))
                        super().save(n)
        except Exception as ex:
            print("Error opening file {ex}".format(ex=ex))

    def __update_file(self):
        try:
            with open(self.__file_name, "w") as f:
                lst = self.get_all()
                for node in lst:
                    n = "{nod}, ".format(nod=node.data) if node != lst[-1] else str(node.data)
                    f.write(n)
        except Exception as ex:
            print("Error opening file {ex}".format(ex=ex))

    def __save_node(self, node: Node):
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
