__author__ = 'victor'

from store.repository.BSTFileRepository import BSTFileRepository
from store.controller.BSTController import BSTController
from store.ui.Console import Console


class App(object):
    @classmethod
    def main(cls):
        """Set up the app
        """
        repo = BSTFileRepository("binarySearchTree.txt")

        bst_controller = BSTController(repo)

        console = Console(bst_controller)
        console.run()


if __name__ == '__main__':
    App.main()