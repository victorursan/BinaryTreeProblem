__author__ = 'victor'

import unittest
from tests.store.domain import test_domain
from tests.store.repository import test_repository

all_suites = unittest.TestSuite([test_domain.suite(), test_repository.suite()])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(all_suites)
