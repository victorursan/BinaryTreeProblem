__author__ = 'victor'

import unittest
from tests.store.domain.BinarySearchTreeTestCase import BinarySearchTreeTestCase
from tests.store.domain.NodeTestCase import NodeTestCase


def suite():
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().loadTestsFromTestCase(BinarySearchTreeTestCase))
    suites.addTests(unittest.TestLoader().loadTestsFromTestCase(NodeTestCase))
    return suites