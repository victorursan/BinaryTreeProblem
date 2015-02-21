__author__ = 'victor'

import unittest
from tests.store.domain import test_domain

all_suites = unittest.TestSuite([test_domain.suite()])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(all_suites)
