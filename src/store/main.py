__author__ = 'victor'

from store.controller.BSTController import BSTController
from store.repository.Repository import Repository
from store.ui.Console import Console


class App(object):
    @classmethod
    def main(cls):
        """Set up the app
        """
        repo = Repository()

        bst_controller = BSTController(repo)

        console = Console(bst_controller)
        console.run()


if __name__ == '__main__':
    App.main()