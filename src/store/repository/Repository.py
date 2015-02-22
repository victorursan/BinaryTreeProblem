__author__ = 'victor'


class Repository(object):
    def __init__(self):
        """Initializes the repository
        """
        self.__items = []

    def save(self, item):
        """Saves a new item in the repository
        :param item: the new item that is added to repo
        """
        if item not in self.__items:
            self.__items.append(item)
        else:
            return

    def delete(self, item):
        """Deletes a item from the repo
        :param item: the item we want to remove
        """
        if item in self.__items:
            self.__items.remove(item)
        else:
            return

    def update(self, item1, item2):
        """Updates a replaces an item with another one
        :param item1: the item we want to replace
        :param item2: the item with which we want to replace it
        """
        if item1 in self.__items:
            index = self.__items.index(item1)
            self.__items[index] = item2
        else:
            self.save(item2)

    def find(self, item):
        """Returns the index of a given item
        :param item: the item we want to find
        :returns: the item's index if or None if the item is not in the repo
        """
        if item in self.__items:
            return self.__items.index(item)
        return None

    def size(self):
        """Returns the size of the repo
        :returns: the size of the repo
        """
        return len(self.__items)

    def get_all(self):
        """Returns a the list of all items in the repo
        :returns: a list with all the items
        """
        return self.__items